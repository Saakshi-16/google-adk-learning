# Chapter 6: Stateful Workflows in Google ADK

## Overview

One of the most powerful features of the Google Agent Development Kit (ADK) is its support for stateful workflows. Unlike traditional applications that execute a single function, ADK applications execute a sequence of connected workflow nodes while maintaining application state.

During this learning journey, I explored how workflow graphs are constructed, how execution flows between nodes, and how state is preserved throughout the lifecycle of an AI agent.

The Ambient Expense Agent developed during this project is an example of a workflow-based AI application where multiple components cooperate to process an expense request.

---

# What is a Workflow?

A workflow is an ordered sequence of tasks that an AI agent performs to accomplish a goal.

Instead of asking the language model to perform everything in one prompt, the work is divided into multiple independent steps.

Each step performs a specific responsibility.

Example:

User submits expense

↓

Extract expense information

↓

Check approval policy

↓

Request approval (if required)

↓

Return final result

This modular approach improves readability, maintainability, and scalability.

---

# Why Stateful Workflows?

Many real-world business processes cannot be completed in a single interaction.

Examples include:

- Expense approvals
- Travel requests
- Insurance claims
- Customer onboarding
- Loan processing

These workflows require the application to remember previous information while waiting for the next step.

A stateful workflow preserves this information automatically.

---

# Workflow Components

Google ADK represents workflows using several building blocks.

## START Node

Every workflow begins at the START node.

The START node acts as the entry point for workflow execution.

Example:

```
START

↓

Expense Analyzer
```

No application logic is written inside START.

Its purpose is simply to indicate where execution begins.

---

## Workflow Nodes

A workflow consists of multiple nodes.

Each node performs one specific task.

Examples include:

- AI reasoning
- Python functions
- Tool execution
- API calls
- Human approval

In the Ambient Expense Agent two primary nodes were used:

- Expense Analyzer
- Process Expense

Separating responsibilities into different nodes results in cleaner application architecture.

---

## Edges

Edges connect workflow nodes together.

They determine how execution moves from one node to another.

Example:

```
START

↓

Expense Analyzer

↓

Process Expense

↓

END
```

Edges allow workflows to be represented as directed graphs.

---

# LlmAgent

The first node in the Ambient Expense Agent is an LlmAgent.

Responsibilities include:

- Understanding user input
- Extracting structured information
- Generating AI responses

Example:

```python
expense_analyzer = LlmAgent(...)
```

The agent extracts:

- Expense description
- Expense amount
- Expense category

This structured information is then passed to the next workflow node.

---

# Structured Output

Instead of returning plain text, the LlmAgent returns structured data using an output schema.

Example:

```python
class ExpenseDetails(BaseModel):
    description: str
    amount: float
    category: str
```

Example output:

```json
{
    "description":"Client Dinner",
    "amount":150,
    "category":"Food"
}
```

Structured outputs simplify downstream workflow processing.

---

# Function Nodes

The second node of the workflow is a Python function.

Example:

```python
async def process_expense(...)
```

Responsibilities include:

- Reading extracted data
- Checking approval rules
- Requesting human approval when necessary
- Returning the final workflow result

Unlike the LlmAgent, this node performs business logic rather than AI reasoning.

---

# Context

The Context object stores information during workflow execution.

It allows different nodes to share information without manually passing variables between functions.

Context may contain:

- User information
- Workflow state
- Session data
- Resume inputs
- Approval responses

This makes workflow execution more organized.

---

# State Management

State management allows workflows to pause and continue later.

For example:

Expense submitted

↓

Workflow pauses

↓

Manager approves

↓

Workflow resumes

↓

Expense completed

Without state management, the application would need to restart from the beginning after every interruption.

---

# Events

Workflow nodes communicate through events.

Examples include:

- User input
- Model response
- Approval request
- Workflow completion

Events make workflow execution asynchronous and flexible.

---

# Human Approval

The Ambient Expense Agent contains a Human-in-the-Loop approval stage.

If the expense amount exceeds the configured limit, the workflow pauses and waits for approval.

Example:

```
Expense = $150

↓

Approval Required

↓

Manager approves

↓

Workflow continues
```

This demonstrates how AI systems can safely incorporate human decision-making into automated processes.

---

# Workflow Execution in the Ambient Expense Agent

The workflow implemented during this project follows these steps:

1. User submits an expense.

2. Gemini extracts:
   - Description
   - Amount
   - Category

3. The structured output is passed to the processing node.

4. Business rules are evaluated.

5. If approval is required, the workflow pauses.

6. Otherwise, the expense is automatically approved.

7. The workflow returns the final result.

This design separates AI reasoning from business logic, resulting in a cleaner architecture.

---

# Advantages of Stateful Workflows

Stateful workflows provide several advantages:

- Modular architecture
- Better scalability
- Easier debugging
- Human approval support
- Session management
- Clear execution flow
- Reusable workflow nodes

These advantages make workflow-based AI systems suitable for enterprise applications.

---

# Challenges Faced During Development

While implementing the Ambient Expense Agent, I explored workflow execution using the ADK Playground.

I inspected workflow graphs, execution traces, and session information to understand how data moved between nodes.

I also investigated Human-in-the-Loop behaviour when testing approval requests. Although I encountered a compatibility issue related to the ADK version used during the codelab, the debugging process helped me better understand workflow execution, state management, and interrupt-based processing.

---

# My Learning During This Chapter

This chapter gave me practical experience in building workflow-driven AI applications.

I learned how Google ADK organizes AI applications into modular workflow nodes connected through edges, while maintaining state using context and sessions.

Building the Ambient Expense Agent helped me understand the difference between AI reasoning and business logic, and demonstrated how stateful workflows can automate real-world business processes.

---

# Key Takeaways

- Workflows divide AI applications into manageable tasks.
- START marks the beginning of workflow execution.
- Nodes perform individual responsibilities.
- Edges define execution flow.
- LlmAgent performs AI reasoning.
- Function nodes execute business logic.
- Context stores workflow information.
- Stateful workflows support interruptions and resumption.
- Structured outputs simplify downstream processing.
- Workflow graphs improve application organization.

---

# References

- Google Agent Development Kit Documentation
- Google Developer Program Learning Path
- Gemini API Documentation
