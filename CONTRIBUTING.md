# Contributing to Open AI Toolkit

Thanks for your interest in contributing to Open AI Toolkit!

Contributions of all sizes are welcome, including bug fixes, documentation improvements, new features, and ideas.

## Getting Started

1. Fork this repository.

2. Clone your fork:

```bash
git clone https://github.com/YOUR-USERNAME/open-ai-toolkit.git
```

3. Enter the project directory:

```bash
cd open-ai-toolkit
```

4. Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

5. Make and test your changes.

6. Commit your changes:

```bash
git commit -m "Describe your change"
```

7. Push your branch:

```bash
git push origin feature/your-feature-name
```

8. Open a pull request.

## Development Requirements

You will need:

- Python 3.10 or newer
- Ollama
- At least one local Ollama model, such as `llama3.2`

Run the application with:

```bash
python app.py
```

## What You Can Contribute

Contributions are welcome in areas such as:

- Support for additional local AI backends
- Streaming model responses
- Conversation history
- Command-line model selection
- Configuration support
- Improved error handling
- Automated tests
- Documentation improvements
- Command-line interface improvements
- Web interface development

## Pull Requests

Please keep pull requests focused on one change where possible.

Before submitting a pull request:

- Make sure the application still runs correctly.
- Test your changes locally.
- Keep the code readable and documented.
- Clearly explain what your change does.
- Mention any related GitHub issue.

## Reporting Bugs

If you find a bug, please open a GitHub Issue.

Include as much relevant information as possible:

- Operating system
- Python version
- Ollama version
- Model being used
- Steps required to reproduce the problem
- Expected behavior
- Actual behavior
- Relevant error messages

Please do not include passwords, API keys, tokens, or other sensitive information.

## Feature Requests

Feature suggestions are welcome.

When opening a feature request, explain:

- What feature you would like
- What problem it solves
- Why it would be useful
- How you expect it to work

## Development Philosophy

Open AI Toolkit aims to remain:

- Simple to install
- Easy to understand
- Friendly to new contributors
- Useful for local AI experimentation
- Independent of mandatory commercial AI APIs

New features should avoid unnecessary complexity whenever possible.

## Code Style

When contributing Python code:

- Use clear variable and function names.
- Keep functions focused on a specific task.
- Add comments where behavior may not be obvious.
- Avoid adding dependencies unless they provide a clear benefit.
- Maintain compatibility with Python 3.10 or newer.

## Security

If you discover a security issue, avoid publishing sensitive exploit details in a public issue.

Never commit:

- API keys
- Authentication tokens
- Passwords
- Private model credentials
- Personal or confidential information

## License

By contributing to Open AI Toolkit, you agree that your contributions will be distributed under the project's MIT License.

## Thank You

Thank you for helping improve Open AI Toolkit and making local AI tools more accessible to developers and learners.
