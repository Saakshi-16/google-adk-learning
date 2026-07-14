# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import LlmAgent
from google.adk.agents.context import Context
from google.adk.apps import App
from google.adk.events.event import Event
from google.adk.events.request_input import RequestInput
from google.adk.models import Gemini
from google.adk.workflow import Workflow, START
from google.genai import types
from pydantic import BaseModel


class ExpenseDetails(BaseModel):
    description: str
    amount: float
    category: str


expense_analyzer = LlmAgent(
    name="expense_analyzer",
    model=Gemini(
        model="gemini-flash-latest",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="Extract expense details (description, amount, category) from the user's message. If any detail is missing, guess or use 'unknown'.",
    output_schema=ExpenseDetails,
)


async def process_expense(ctx: Context, node_input: dict):
    # node_input is the dict returned by expense_analyzer
    description = node_input.get("description", "unknown")
    amount = node_input.get("amount", 0.0)
    category = node_input.get("category", "unknown")

    # Limit check for human-in-the-loop step
    if amount > 100.0:
        if not ctx.resume_inputs or "approved" not in ctx.resume_inputs:
            # Yield RequestInput for human-in-the-loop approval
            yield RequestInput(
                interrupt_id="approved",
                message=f"Expense of ${amount:.2f} for '{description}' ({category}) exceeds the $100 limit. Do you approve? (yes/no)"
            )
            return
        
        # User has responded
        user_response = ctx.resume_inputs["approved"]
        if user_response.lower().strip() in ("yes", "y", "approve", "approved"):
            approval_status = "Approved"
        else:
            approval_status = "Rejected"
    else:
        approval_status = "Auto-Approved"

    result_msg = f"Expense of ${amount:.2f} for '{description}' is {approval_status}."
    
    # Yield content event for web UI display, and final output event
    yield Event(
        content=types.Content(
            role="model",
            parts=[types.Part.from_text(text=result_msg)]
        )
    )
    yield Event(
        output={
            "description": description,
            "amount": amount,
            "category": category,
            "status": approval_status
        }
    )


root_agent = Workflow(
    name="root_agent",
    edges=[
        (START, expense_analyzer),
        (expense_analyzer, process_expense),
    ],
)


app = App(
    root_agent=root_agent,
    name="app",
)
