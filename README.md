# Open AI Toolkit

![Tests](https://github.com/shashanknaik808/open-ai-toolkit/actions/workflows/tests.yml/badge.svg)

A lightweight, open-source Python toolkit for interacting with local AI models through Ollama.

The project provides a simple command-line interface for experimenting with locally hosted language models without requiring a cloud API key.

## Features

- Run AI models locally through Ollama
- Interactive command-line chat
- Streaming AI responses
- Automatically detect installed Ollama models
- Select between installed models
- No external Python dependencies
- Simple Python codebase for learning and experimentation
- Automated testing with GitHub Actions
- Open source under the MIT License

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

### 3. Pull the default model

```bash
ollama pull llama3.2
```

You can also install additional models supported by Ollama.

For example:

```bash
ollama pull mistral
```

### 4. Run Open AI Toolkit

```bash
python app.py
```

## Usage

Start the toolkit:

```bash
python app.py
```

The toolkit will connect to the locally running Ollama server and detect the models installed on your system.

You can then select a model and enter a prompt.

Example:

```text
Open AI Toolkit
Local AI command-line interface powered by Ollama.

Available models:

1. llama3.2
2. mistral

Select a model: 1

Using model: llama3.2

You: Explain recursion in simple terms.

AI: Recursion is when a function solves a problem by calling itself with a smaller version of the same problem.
```

Type:

```text
exit
```

to quit the toolkit.

## Model Selection

Open AI Toolkit can detect models installed through Ollama.

To see the models available directly through Ollama, run:

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

Restart the toolkit and the installed model will become available for selection.

## Streaming Responses

Open AI Toolkit uses Ollama's streaming API.

Instead of waiting for the entire response to finish, generated text is displayed as it arrives from the model.

This provides a more responsive command-line chat experience.

## Running Tests

The project includes automated tests using Python's built-in `unittest` framework.

Run the tests with:

```bash
python -m unittest -v tests.test_app
```

The tests verify core functionality including:

- Default model configuration
- Ollama model discovery
- Streaming response handling
- Ollama API error handling

## Continuous Integration

Automated tests run through GitHub Actions whenever code is pushed or a pull request is opened.

The current CI matrix tests the project with:

- Python 3.10
- Python 3.11

The test status is displayed by the badge at the top of this README.

## Project Structure

```text
open-ai-toolkit/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   └── test_app.py
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── app.py
```

## Ollama API

By default, Open AI Toolkit communicates with Ollama at:

```text
http://localhost:11434
```

The toolkit uses Ollama's local API for model discovery and text generation.

Because Ollama runs locally, a cloud AI API key is not required.

## Troubleshooting

### Cannot connect to Ollama

Make sure Ollama is installed and running.

You can check your installed models with:

```bash
ollama list
```

If Ollama is not running, start it before launching the toolkit.

### Model not found

Check which models are installed:

```bash
ollama list
```

If necessary, download the model:

```bash
ollama pull llama3.2
```

Then run the toolkit again.

## Contributing

Contributions are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Run the tests.
5. Commit your changes.
6. Push your branch.
7. Open a pull request.

See `CONTRIBUTING.md` for the complete contribution guidelines.

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

## Author

Created and maintained by **Shashank Naik**.

## Project Status

Open AI Toolkit is under active development.

Current functionality includes local Ollama integration, automatic model discovery, model selection, streaming responses, automated tests, and GitHub Actions continuous integration.
