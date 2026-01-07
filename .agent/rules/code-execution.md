# Code Execution Rules

This document outlines the protocols and standards for executing code and terminal commands within this project.

## 1. Safety & Permissions
- **Destructive Commands**: Always request explicit user approval before running commands that delete files (e.g., `rm -rf`), modify system configurations, or drop database tables.
- **Auto-Run**: Only mark commands as `SafeToAutoRun` if they are read-only (e.g., `ls`, `cat`, `grep`) or standard build/test commands that do not permanently alter critical state.

## 2. Environment Management
- **Verified Environment**: Ensure all Python commands are executed within the project's virtual environment (e.g., using `poetry run` or identifying the venv path).
- **Directory Context**: Always verify the current working directory (`Cwd`) before executing path-dependent scripts.

## 3. Execution Workflow
1.  **Plan**: Identify the necessary command and its arguments.
2.  **Execute**: Run the command using the `run_command` tool.
3.  **Monitor**: For background processes, use `command_status` to check progress.
4.  **Verify**: Analyzing the command's standard output or error logs to confirm success.
    - *Success*: Proceed to the next step.
    - *Failure*: analyze the error, propose a fix, and retry.

## 4. Testing Protocols
- **Unit Tests**: Run relevant unit tests after every logic change.
- **Integration Tests**: Run integration tests before marking a feature as complete.
- **Failing Tests**: Do not ignore failing tests. Fix the code or update the test if the requirements have changed.

## 5. REPL & Interactive Scripts
- Use `send_command_input` to interact with running processes (e.g., Python shells, database prompts).
- Always terminate interactive sessions properly to free up resources.