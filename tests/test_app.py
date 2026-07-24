"""
Open AI Toolkit

A lightweight command-line toolkit for interacting with
local AI models through Ollama.
"""

import json
import urllib.error
import urllib.request


OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2"


def ollama_request(path, data=None):
    """Create and send a request to the local Ollama API."""

    url = OLLAMA_URL + path

    if data is None:
        request = urllib.request.Request(
            url,
            method="GET",
        )
    else:
        request = urllib.request.Request(
            url,
            data=json.dumps(data).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
            },
            method="POST",
        )

    try:
        return urllib.request.urlopen(request)

    except urllib.error.HTTPError as error:
        try:
            response = json.loads(
                error.read().decode("utf-8")
            )
            message = response.get("error", str(error))
        except (json.JSONDecodeError, UnicodeDecodeError):
            message = str(error)

        raise RuntimeError(message) from error

    except urllib.error.URLError as error:
        raise RuntimeError(
            "Could not connect to Ollama. "
            "Make sure Ollama is installed and running."
        ) from error


def list_models():
    """Return the names of locally installed Ollama models."""

    try:
        with ollama_request("/api/tags") as response:
            data = json.loads(
                response.read().decode("utf-8")
            )

    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise RuntimeError(
            "Ollama returned an invalid response."
        ) from error

    return [
        model["name"]
        for model in data.get("models", [])
        if "name" in model
    ]


def generate(prompt, model=DEFAULT_MODEL):
    """Generate and stream a response from an Ollama model."""

    data = {
        "model": model,
        "prompt": prompt,
        "stream": True,
    }

    with ollama_request("/api/generate", data) as response:
        for line in response:
            if not line:
                continue

            try:
                chunk = json.loads(
                    line.decode("utf-8")
                )
            except (json.JSONDecodeError, UnicodeDecodeError) as error:
                raise RuntimeError(
                    "Ollama returned an invalid response."
                ) from error

            if "error" in chunk:
                raise RuntimeError(chunk["error"])

            text = chunk.get("response", "")

            if text:
                print(
                    text,
                    end="",
                    flush=True,
                )

            if chunk.get("done", False):
                break


def choose_model():
    """Allow the user to select an installed Ollama model."""

    try:
        models = list_models()
    except RuntimeError as error:
        print(f"Error: {error}")
        return DEFAULT_MODEL

    if not models:
        print(
            "No installed Ollama models were found. "
            f"Using default model: {DEFAULT_MODEL}"
        )
        return DEFAULT_MODEL

    print("\nAvailable models:")

    for index, model in enumerate(models, start=1):
        print(f"{index}. {model}")

    while True:
        choice = input(
            "\nSelect a model "
            f"[1-{len(models)}] "
            f"or press Enter for {models[0]}: "
        ).strip()

        if not choice:
            return models[0]

        try:
            index = int(choice) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 <= index < len(models):
            return models[index]

        print("Invalid model selection.")


def main():
    """Run the Open AI Toolkit command-line interface."""

    print("=" * 50)
    print("Open AI Toolkit")
    print("=" * 50)

    print(
        "\nLocal AI command-line interface powered by Ollama."
    )

    model = choose_model()

    print(f"\nUsing model: {model}")
    print("Type /model to change models.")
    print("Type 'exit' to quit.")

    while True:
        try:
            prompt = input("\nYou: ").strip()

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not prompt:
            continue

        if prompt.lower() in {
            "exit",
            "quit",
        }:
            print("Goodbye!")
            break

        if prompt.lower() == "/model":
            model = choose_model()
            print(f"\nUsing model: {model}")
            continue

        print("\nAI: ", end="", flush=True)

        try:
            generate(
                prompt,
                model,
            )
            print()

        except RuntimeError as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()
