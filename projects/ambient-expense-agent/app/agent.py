# ruff: noqa
# Copyright 2026 Google LLC

import re

from google.adk.agents import LlmAgent
from google.adk.agents.context import Context
from google.adk.apps import App
from google.adk.events.event import Event
from google.adk.events.request_input import RequestInput
from google.adk.models import Gemini
from google.adk.workflow import Workflow, START, node
from google.genai import types
from pydantic import BaseModel


def redact_pii(text: str) -> str:
    """Redacts SSNs and credit card numbers."""

    if not text:
        return text

    # SSN
    text = re.sub(
        r"\b\d{3}-\d{2}-\d{4}\b",
        "[REDACTED_SSN]",
        text,
    )

    # Credit Card
    text = re.sub(
        r"\b(?:\d[ -]*?){13,16}\b",
        "[REDACTED_CARD]",
        text,
    )

    return text


def detect_prompt_injection(text: str) -> bool:
    """Simple prompt injection detector."""

    if not text:
        return False

    patterns = [
        "ignore previous",
        "ignore all",
        "bypass",
        "override",
        "auto approve",
        "approve this",
        "developer instructions",
        "system prompt",
    ]

    text = text.lower()

    return any(pattern in text for pattern in patterns)


class ExpenseDetails(BaseModel):
    description: str
    amount: float
    category: str


expense_analyzer = LlmAgent(
    name="expense_analyzer",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=(
        "Extract expense details (description, amount, category) "
        "from the user's message. If any detail is missing, "
        "guess or use 'unknown'."
    ),
    output_schema=ExpenseDetails,
)


@node
def security_screen(node_input: dict):

    description = node_input.get("description", "")

    cleaned = redact_pii(description)

    injection = detect_prompt_injection(description)

    node_input["description"] = cleaned
    node_input["prompt_injection"] = injection

    print("\n===== SECURITY SCREEN =====")
    print("Original:", description)
    print("Redacted:", cleaned)
    print("Prompt Injection:", injection)
    print("===========================\n")

    return Event(output=node_input)


async def process_expense(ctx: Context, node_input: dict):

    print("\n==============================")
    print("DEBUG process_expense called")
    print("DEBUG resume_inputs:", ctx.resume_inputs)
    print("==============================\n")

    description = node_input.get("description", "unknown")
    amount = node_input.get("amount", 0.0)
    category = node_input.get("category", "unknown")

    if node_input.get("prompt_injection"):

        print("⚠ SECURITY ALERT: Prompt Injection detected!")

        yield RequestInput(
            interrupt_id="approved",
            message=(
                "Security Alert!\n\n"
                "Prompt injection detected.\n"
                "Manual approval required.\n\n"
                "Type YES or NO."
            ),
        )
        return

    if amount > 100:

        if not ctx.resume_inputs or "approved" not in ctx.resume_inputs:
            print("DEBUG -> Waiting for approval")

            yield RequestInput(
                interrupt_id="approved",
                message=(
                    f"Expense of ${amount:.2f} for "
                    f"'{description}' ({category}) exceeds "
                    "the $100 limit.\n\n"
                    "Type YES or NO."
                ),
            )
            return

        print("DEBUG resumed with:", ctx.resume_inputs)

        user_response = ctx.resume_inputs["approved"]

        print("DEBUG user response:", user_response)

        if user_response.lower().strip() in (
            "yes",
            "y",
            "approve",
            "approved",
        ):
            approval_status = "Approved"
        else:
            approval_status = "Rejected"

    else:
        approval_status = "Auto-Approved"

    result_msg = (
        f"Expense of ${amount:.2f} "
        f"for '{description}' is {approval_status}."
    )

    yield Event(
        content=types.Content(
            role="model",
            parts=[
                types.Part.from_text(text=result_msg)
            ],
        )
    )

    yield Event(
        output={
            "description": description,
            "amount": amount,
            "category": category,
            "status": approval_status,
        }
    )


root_agent = Workflow(
    name="root_agent",
    edges=[
        (START, expense_analyzer),
        (expense_analyzer, security_screen),
        (security_screen, process_expense),
    ],
)


app = App(
    root_agent=root_agent,
    name="app",
)