# Chapter 7: Human-in-the-Loop (HITL)

## Overview

Human-in-the-Loop (HITL) is a design pattern where an AI system pauses its execution and requests input from a human before continuing.

This approach combines the speed and intelligence of AI with human judgment, making it suitable for business processes that involve risk, compliance, financial approval, or sensitive decisions.

During this learning journey, I implemented a Human-in-the-Loop workflow in the Ambient Expense Agent using Google ADK.

---

# What is Human-in-the-Loop?

Human-in-the-Loop (HITL) is a workflow in which an AI agent requests approval, confirmation, or additional information from a human before completing a task.

Instead of allowing AI to make every decision independently, certain actions require human validation.

Typical workflow:

User submits request

↓

AI processes request

↓

Human approval required

↓

Human responds

↓

Workflow resumes

↓

Final result returned

This ensures that important decisions remain under human control.

---

# Why Human Approval is Important

Many business applications cannot rely entirely on automated decisions.

Examples include:

- Expense approvals
- Loan approvals
- Insurance claims
- Medical recommendations
- Legal document review
- Financial transactions

In these scenarios, AI assists with analysis while humans make the final decision.

This reduces operational risk and increases trust in AI systems.

---

# Human-in-the-Loop in Google ADK

Google ADK provides built-in support for Human-in-the-Loop workflows using interrupt-based execution.

Instead of completing the workflow immediately, the agent can pause execution and wait for a response.

This makes it possible to build enterprise workflows where AI and humans collaborate.

---

# RequestInput

Google ADK uses the `RequestInput` event to pause a workflow.

Example:

```python
yield RequestInput(
    interrupt_id="approved",
    message="Do you approve this expense?"
)
```

When this event is triggered:

- The workflow pauses
- A request is shown to the user
- Execution waits for a response
- The workflow resumes after receiving input

This mechanism forms the foundation of Human-in-the-Loop workflows.

---

# Resume Inputs

After the user provides a response, ADK stores it in `resume_inputs`.

Example:

```python
ctx.resume_inputs
```

The workflow reads the value and continues execution.

Example:

```python
user_response = ctx.resume_inputs["approved"]
```

The application can then determine whether to approve or reject the request.

---

# Human Approval Logic in the Ambient Expense Agent

In the Ambient Expense Agent, the workflow checks the expense amount.

If the amount is less than or equal to the approval limit:

```
Expense = $80

↓

Automatically Approved
```

If the amount exceeds the approval limit:

```
Expense = $150

↓

Human Approval Required

↓

Manager responds

↓

Workflow continues
```

This demonstrates how AI can automate routine decisions while escalating important ones to humans.

---

# Workflow Execution

The approval workflow implemented during this project follows these steps:

1. User submits an expense.

2. Gemini extracts:
   - Description
   - Amount
   - Category

3. Business rules are evaluated.

4. If the amount exceeds the configured threshold, the workflow pauses.

5. A Human Approval request is generated.

6. The workflow waits for the approval response.

7. The final approval status is returned.

This workflow separates AI reasoning from human decision-making.

---

# Enterprise Applications

Human-in-the-Loop workflows are widely used across industries.

Examples include:

## Finance

- Expense approvals
- Payment authorization
- Fraud investigation

---

## Healthcare

- Clinical review
- Prescription approval
- Diagnosis validation

---

## Human Resources

- Resume screening
- Hiring approval
- Leave requests

---

## Legal

- Contract review
- Compliance verification
- Document approval

---

## Customer Support

- Escalation of complex support requests
- Refund approvals
- Complaint resolution

---

# My Implementation Experience

While implementing the Ambient Expense Agent, I created a workflow that paused whenever an expense exceeded the configured approval limit.

The workflow successfully generated the approval request using `RequestInput`.

During testing in the ADK Playground, I verified that the workflow reached the approval stage and paused correctly.

I also investigated an issue where the workflow did not resume after submitting the approval response. Through debugging, I learned how ADK manages workflow interruptions, resume inputs, execution traces, and session state.

Although the resume behavior appeared to be related to the ADK version used during the codelab, the implementation provided valuable insight into how interrupt-driven workflows are designed and executed.

---

# Benefits of Human-in-the-Loop

Some important advantages include:

- Increased reliability
- Better decision quality
- Reduced operational risk
- Improved compliance
- Human oversight
- Greater trust in AI systems

These benefits make HITL a common requirement for enterprise AI applications.

---

# Challenges Faced

While implementing Human-in-the-Loop, I encountered several practical challenges.

I investigated:

- Workflow interruptions
- RequestInput behavior
- Resume inputs
- Session management
- Execution traces
- ADK Playground debugging

These debugging activities helped me understand the internal execution model of Google ADK beyond simply writing code.

---

# My Learning During This Chapter

This chapter introduced me to one of the most important concepts in enterprise AI development.

I learned that AI systems should not always make autonomous decisions. Instead, Human-in-the-Loop workflows allow AI to perform analysis while humans retain control over important business decisions.

Implementing this workflow in the Ambient Expense Agent gave me practical experience with workflow interruptions, approval requests, session management, and debugging workflow execution using Google ADK.

---

# Key Takeaways

- Human-in-the-Loop combines AI automation with human decision-making.
- Google ADK supports interrupt-based workflows using `RequestInput`.
- `resume_inputs` stores user responses after approval.
- Human approval improves trust, compliance, and reliability.
- Workflow interruptions allow AI systems to pause and continue safely.
- Enterprise AI systems frequently use HITL for high-risk decisions.
- Implementing Human-in-the-Loop provided practical experience with workflow execution and debugging.

---

# References

- Google Agent Development Kit Documentation
- Google Developer Program Learning Path
- Gemini API Documentation
