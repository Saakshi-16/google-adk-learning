# Chapter 2: Google Agent Development Kit (ADK)

## Overview

The Google Agent Development Kit (ADK) is an open-source framework developed by Google for building intelligent AI agents. It provides developers with reusable components that simplify the creation of production-ready AI applications powered by Gemini models.

Instead of manually managing prompts, sessions, workflows, and tool execution, ADK provides an organized architecture that allows developers to focus on the business logic of their AI applications.

During this learning journey, I used Google ADK to build an Ambient Expense Agent that extracts expense details, performs workflow execution, and supports Human-in-the-Loop approval.

---

# What is Google ADK?

Google Agent Development Kit (ADK) is a Python framework for developing AI Agents using Google's Gemini models.

It provides built-in support for:

- AI Agents
- Workflow execution
- Tool calling
- Stateful conversations
- Session management
- Event handling
- Human approval workflows
- FastAPI integration

The framework abstracts much of the complexity involved in AI application development.

---

# Why Google ADK?

Traditional AI applications often require developers to manually handle:

- Prompt engineering
- API requests
- Session tracking
- Context management
- Tool execution
- Workflow orchestration

Google ADK simplifies these tasks by providing reusable building blocks.

Benefits include:

- Cleaner architecture
- Modular code
- Better maintainability
- Easier debugging
- Enterprise-ready workflows

---

# ADK Architecture

Google ADK applications are built around several key components.

## 1. Agent

An Agent is the core intelligence of an AI application.

It receives user input, processes information using a language model, and generates outputs.

Example:

```python
expense_analyzer = LlmAgent(...)
```

The Expense Analyzer in my project extracted:

- Expense description
- Amount
- Category

using Gemini.

---

## 2. LlmAgent

LlmAgent is a predefined ADK component that connects directly to a Gemini model.

Responsibilities include:

- Understanding prompts
- Extracting structured data
- Generating responses
- Producing JSON outputs
- Calling tools when required

In the Ambient Expense Agent, the LlmAgent analyzed user expenses before passing them to the workflow.

---

## 3. Workflow

A Workflow defines how an AI application executes multiple steps.

Instead of executing everything inside one prompt, ADK organizes execution into nodes connected through edges.

Example:

START

↓

Expense Analyzer

↓

Expense Processing

↓

Output

This structure improves readability and maintainability.

---

## 4. Nodes

A node represents one unit of work.

Examples include:

- LLM reasoning
- Python function
- Tool execution
- Human approval
- API call

Each node performs a specific responsibility.

---

## 5. Edges

Edges define how execution moves between nodes.

Example:

START

↓

Expense Analyzer

↓

Process Expense

↓

END

This graph-based execution model makes workflows easier to visualize.

---

## 6. Context

Context stores information while a workflow is running.

It allows different workflow nodes to access shared data.

For example:

- User information
- Previous responses
- Approval status
- Workflow state

Context prevents developers from manually passing variables between every function.

---

## 7. Events

Events are messages exchanged during workflow execution.

Examples include:

- User input
- Model output
- Human approval requests
- Workflow completion

The Ambient Expense Agent generated events whenever an expense was processed.

---

## 8. Sessions

Sessions maintain conversation history.

Without sessions, every user request would be treated independently.

Sessions allow AI Agents to:

- Remember previous interactions
- Continue conversations
- Resume interrupted workflows

ADK automatically manages session storage.

---

## 9. App

The App object connects the workflow to the outside world.

Example:

```python
app = App(
    root_agent=root_agent,
    name="app",
)
```

This object enables the workflow to run inside the ADK Playground and FastAPI server.

---

## 10. Runner

The Runner executes the application.

Responsibilities include:

- Starting workflows
- Managing sessions
- Executing nodes
- Returning outputs

The Runner acts as the execution engine of the application.

---

# Building the Ambient Expense Agent

During this learning project, I implemented an AI-powered expense approval system using Google ADK.

The workflow consisted of:

1. User submits an expense.
2. Gemini extracts expense details.
3. Workflow validates the amount.
4. If the expense exceeds the threshold, Human-in-the-Loop approval is requested.
5. The workflow returns the final approval status.

This project demonstrated how multiple ADK components work together.

---

# Advantages of Google ADK

Some important advantages include:

- Modular architecture
- Workflow-based execution
- Easy integration with Gemini
- Session management
- Human approval support
- Structured outputs
- Event-driven execution
- FastAPI compatibility

These features make ADK suitable for enterprise AI applications.

---

# My Learning During This Chapter

Through this chapter, I gained practical experience with Google's Agent Development Kit and understood how modern AI applications are structured.

I learned how Agents, Workflows, Context, Events, Sessions, and the App object interact to create intelligent AI systems.

Implementing the Ambient Expense Agent helped me understand how workflow-based AI applications differ from traditional prompt-response applications.

The project also introduced me to structured AI development, where each component has a specific responsibility, resulting in cleaner, scalable, and maintainable code.

---

# Key Takeaways

- Google ADK simplifies AI Agent development.
- LlmAgent provides seamless integration with Gemini models.
- Workflow graphs improve application organization.
- Context and Sessions maintain state across workflow execution.
- Events allow communication between workflow components.
- The App object exposes the workflow to external applications.
- Google ADK provides enterprise-ready features for AI application development.

---

# References

- Google Agent Development Kit Documentation
- Google Gemini API Documentation
- Google Developer Program Learning Path
