# Open AI Toolkit

A lightweight, open-source Python toolkit for interacting with local AI models through Ollama.

The project provides a simple command-line interface for experimenting with locally hosted language models without requiring a cloud API key.

## Features

- Run AI models locally through Ollama
- Interactive command-line chat
- No external Python dependencies
- Configurable Ollama model
- Simple Python codebase for learning and experimentation
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

Clone the repository:

```bash
git clone https://github.com/shashanknaik808/open-ai-toolkit.git
cd open-ai-toolkit
```

Make sure Ollama is installed and running.

Pull the default model:

```bash
ollama pull llama3.2
```

Then start the toolkit:

```bash
python app.py
```

## Usage

After starting the program, enter a prompt:

```text
Open AI Toolkit
Type 'exit' to quit.

You: Explain recursion in simple terms.

AI: ...
```

Enter `exit` or `quit` to close the program.

## How It Works

The application communicates with Ollama's local HTTP API at:

```text
http://localhost:11434/api/generate
```

Prompts are sent to the locally running model and the generated response is displayed in the terminal.

Because inference runs through Ollama, prompts do not require a commercial cloud AI API.

## Project Structure

```text
open-ai-toolkit/
├── app.py
├── README.md
├── LICENSE
└── .gitignore
```

## Roadmap

Future improvements may include:

- Model selection from the command line
- Streaming responses
- Conversation history
- Configuration files
- Improved error handling
- Support for additional local inference backends
- Web interface

## Contributing

Contributions, bug reports, and feature suggestions are welcome.

If you would like to contribute, fork the repository, create a branch, make your changes, and open a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
