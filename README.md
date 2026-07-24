# Open AI Toolkit

![Tests](https://github.com/shashanknaik808/open-ai-toolkit/actions/workflows/tests.yml/badge.svg)

A lightweight, open-source Python toolkit for interacting with local AI models through Ollama.

Open AI Toolkit provides a simple command-line interface for running locally hosted language models with model selection, streaming responses, and conversation history — without requiring a commercial cloud AI API key.

## Features

- Run AI models locally through Ollama
- Interactive command-line chat
- Automatic discovery of installed Ollama models
- Interactive model selection
- Command-line model selection
- Streaming AI responses
- Conversation history during the current session
- Clear conversation history without restarting
- No external runtime Python dependencies
- CLI `--help` and `--version` commands
- Automated unit tests
- GitHub Actions continuous integration
- Python package build and installation validation
- MIT licensed and open source

## Requirements

- Python 3.10 or newer
- Ollama
- At least one Ollama model installed

The default model is:

```text
llama3.2
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shashanknaik808/open-ai-toolkit.git
cd open-ai-toolkit
```

### 2. Install Ollama

Install Ollama and make sure it is running on your computer.

### 3. Install a model

Pull the default model:

```bash
ollama pull llama3.2
```

You can install additional models as well:

```bash
ollama pull mistral
```

### 4. Run the toolkit

From the repository:

```bash
python app.py
```

## Install as a Python Package

Open AI Toolkit includes a `pyproject.toml` configuration and can be installed locally as a Python package.

From the repository directory:

```bash
pip install .
```

After installation, launch it with:

```bash
open-ai-toolkit
```

## Command-Line Options

Display help:

```bash
open-ai-toolkit --help
```

Display the installed toolkit version:

```bash
open-ai-toolkit --version
```

Start with a specific Ollama model:

```bash
open-ai-toolkit --model llama3.2
```

For example:

```bash
open-ai-toolkit --model mistral
```

Using `--model` skips the interactive model-selection screen.

## Usage

Start normally:

```bash
open-ai-toolkit
```

The toolkit detects locally installed Ollama models and allows you to choose one.

Example:

```text
==================================================
Open AI Toolkit
==================================================

Local AI command-line interface powered by Ollama.

Available models:
1. llama3.2
2. mistral

Choose a model [1-2] or press Enter for llama3.2: 1

Using model: llama3.2

You: Explain recursion in simple terms.

AI: Recursion is a technique where a function calls itself to solve smaller versions of the same problem.
```

Type:

```text
exit
```

or:

```text
quit
```

to close the toolkit.

## Interactive Commands

While the toolkit is running, you can use:

```text
/model
```

Change the active Ollama model.

```text
/stream
```

Toggle streaming responses on or off.

```text
/clear
```

Clear the current conversation history.

```text
exit
```

Exit Open AI Toolkit.

## Conversation History

Open AI Toolkit maintains conversation history during the current session.

For example:

```text
You: My name is Shashank.

AI: Nice to meet you, Shashank.

You: What is my name?

AI: Your name is Shashank.
```

Previous user and assistant messages are included when constructing subsequent prompts.

Use:

```text
/clear
```

to reset the conversation context.

Conversation history currently exists only for the active session and is not permanently stored on disk.

## Model Selection

Open AI Toolkit automatically discovers models installed through Ollama.

To view your installed models directly:

```bash
ollama list
```

Install another model with:

```bash
ollama pull MODEL_NAME
```

For example:

```bash
ollama pull mistral
```

You can then select the model interactively or start directly with:

```bash
open-ai-toolkit --model mistral
```

## Streaming Responses

Streaming is enabled by default.

Instead of waiting for an entire model response to finish, generated text is displayed as Ollama produces it.

Streaming can be toggled during a session with:

```text
/stream
```

## Ollama API

By default, Open AI Toolkit communicates with the local Ollama API at:

```text
http://localhost:11434
```

The toolkit currently uses Ollama endpoints for:

- Discovering installed models
- Generating responses
- Streaming generated responses

Because inference runs through your local Ollama installation, Open AI Toolkit does not require a commercial cloud AI API key.

## Running Tests

The project uses Python's built-in `unittest` framework.

Run the test suite with:

```bash
python -m unittest -v tests.test_app
```

The tests cover core functionality including:

- Default model configuration
- Ollama model discovery
- Standard generation
- Streaming generation
- Ollama error handling
- Prompt construction
- Conversation-history construction

## Continuous Integration

GitHub Actions automatically tests the project whenever code is pushed or a pull request is opened.

The current CI matrix validates:

- Python 3.10
- Python 3.11

CI also verifies that:

- Unit tests pass
- The Python package builds successfully
- The generated wheel installs successfully
- `open-ai-toolkit --help` works
- `open-ai-toolkit --version` works

The current build status is displayed by the badge at the top of this README.

## Project Structure

```text
open-ai-toolkit/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   └── test_app.py
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── app.py
└── pyproject.toml
```

## Troubleshooting

### Cannot connect to Ollama

Check that Ollama is installed and running.

Verify your models with:

```bash
ollama list
```

Open AI Toolkit expects Ollama to be available at:

```text
http://localhost:11434
```

### Model not found

Check installed models:

```bash
ollama list
```

If necessary, install one:

```bash
ollama pull llama3.2
```

Then restart Open AI Toolkit.

### Check the toolkit version

Run:

```bash
open-ai-toolkit --version
```

## Contributing

Contributions, bug reports, documentation improvements, and feature suggestions are welcome.

A typical contribution workflow is:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Run the test suite.
5. Commit your changes.
6. Push your branch.
7. Open a pull request.

See `CONTRIBUTING.md` for complete contribution guidelines.

## Roadmap

Potential future improvements include:

- Persistent conversation history
- Configuration files
- Additional local AI backends
- Improved model management
- One-shot prompt mode
- Expanded CLI options
- Additional automated tests
- Web interface

## License

Open AI Toolkit is licensed under the MIT License.

See the `LICENSE` file for details.

## Author

Created and maintained by **Shashank Naik**.

## Project Status

Open AI Toolkit is under active development.

The current version provides a functional local AI command-line environment with Ollama integration, model discovery and selection, streaming responses, conversation context, Python packaging, automated tests, and continuous integration.
