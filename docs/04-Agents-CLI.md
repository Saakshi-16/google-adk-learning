# Chapter 4: Agents CLI & ADK Playground

## Overview

The Google Agent Development Kit (ADK) provides a Command Line Interface (CLI) that simplifies the development, testing, debugging, and deployment of AI agents.

Instead of manually creating API endpoints or writing additional server code, developers can launch and interact with AI agents directly from the terminal using the ADK CLI.

During this learning journey, I used the ADK CLI to run the Ambient Expense Agent locally, visualize workflow graphs, inspect execution traces, debug workflow behavior, and test Human-in-the-Loop interactions.

---

# What is the ADK CLI?

The ADK CLI is the primary command-line tool used for interacting with Google ADK projects.

It allows developers to:

- Run AI agents locally
- Launch the ADK Playground
- Inspect workflow graphs
- Debug workflow execution
- Manage sessions
- Test AI agents before deployment

The CLI eliminates much of the manual setup required during AI application development.

---

# Why Use the ADK CLI?

Without the CLI, developers would need to:

- Configure web servers
- Build custom testing interfaces
- Write debugging utilities
- Manage workflow execution manually

The ADK CLI provides all of these capabilities in a single development environment.

Benefits include:

- Faster development
- Easy testing
- Built-in debugging
- Workflow visualization
- Local execution
- Interactive Playground

---

# Project Structure

A typical ADK project contains files such as:

```
ambient-expense-agent/

├── app/
│   ├── agent.py
│   ├── fast_api_app.py
│   └── app_utils/
│
├── tests/
│
├── pyproject.toml
│
└── README.md
```

The CLI automatically detects the project structure and launches the application.

---

# Running the Agent

The agent can be started locally using the ADK development server.

Example:

```bash
adk web
```

or

```bash
uv run python app/fast_api_app.py
```

This starts a local development server where the AI agent can be tested.

---

# ADK Playground

One of the most useful features of the CLI is the ADK Playground.

The Playground provides a web interface for interacting with AI agents.

It allows developers to:

- Send prompts
- View responses
- Inspect workflow graphs
- Track execution steps
- Monitor sessions
- Debug workflows

During this project, I used the Playground extensively to validate the Ambient Expense Agent.

---

# Workflow Graph

The Playground automatically generates a workflow graph.

The graph displays:

START

↓

Expense Analyzer

↓

Expense Processing

↓

Output

This visualization makes it easier to understand how execution flows between workflow nodes.

---

# Debugging Workflow Execution

The Playground includes execution traces that show:

- Current node
- Workflow state
- Model responses
- Events
- Errors
- Session information

These traces helped me identify problems during development.

---

# Session Management

Each interaction creates a new session.

Sessions maintain:

- Conversation history
- Workflow progress
- User state

This enables AI agents to continue conversations across multiple interactions.

---

# Human-in-the-Loop Testing

One important feature tested during this project was Human-in-the-Loop approval.

The workflow paused when an expense exceeded the approval limit.

The Playground displayed an approval request where a human reviewer could respond.

Although I experienced some compatibility issues with the ADK version used during the project, the workflow correctly reached the approval stage, allowing me to understand how interrupt-based workflows operate.

---

# Debugging Experience

During development I used the Playground to investigate several issues, including:

- Workflow execution
- Missing approval responses
- RequestInput behavior
- Gemini model responses
- Session handling
- API configuration

The execution traces helped identify where the workflow paused and how data moved between workflow nodes.

---

# Benefits of the ADK Playground

The Playground offers several advantages:

- Interactive testing
- Workflow visualization
- Faster debugging
- Execution tracing
- Session inspection
- Local development
- Real-time responses

These features significantly improve the AI development experience.

---

# My Learning During This Chapter

This chapter introduced me to Google's AI development workflow using the ADK CLI and Playground.

I learned how to launch AI agents locally, visualize workflow execution, inspect traces, manage sessions, and debug workflow behavior.

The Playground became an essential tool while building the Ambient Expense Agent because it allowed me to verify each workflow step before moving to the next stage of development.

It also demonstrated how workflow graphs simplify the understanding of complex AI systems.

---

# Key Takeaways

- The ADK CLI simplifies AI agent development.
- The Playground provides an interactive testing environment.
- Workflow graphs visualize execution flow.
- Execution traces help identify workflow issues.
- Sessions maintain conversation state.
- Human-in-the-Loop workflows can be tested directly inside the Playground.
- The CLI significantly reduces development and debugging effort.

---

# References

- Google Agent Development Kit Documentation
- Google ADK Playground
- Google Developer Program Learning Path
