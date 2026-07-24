Fix app syntax error            f"Ollama returned HTTP {error.code}: {error.reason}"
        ) from error

    except urllib.error.URLError as error:
        raise RuntimeError(
            "Could not connect to Ollama. "
            "Make sure Ollama is installed and running."
        ) from error


def list_models():
    """Return the names of locally installed Ollama models."""

    with ollama_request("/api/tags") as response:
        result = json.loads(response.read().decode("utf-8"))

    return [
        model["name"]
        for model in result.get("models", [])
    ]


def generate(prompt: str, model: str):
    """Generate and stream a response from Ollama."""

    data = {
        "model": model,
        "prompt": prompt,
        "stream": True,
    }

    with ollama_request("/api/generate", data) as response:
        for raw_line in response:
            if not raw_line:
                continue

            result = json.loads(raw_line.decode("utf-8"))

            if "error" in result:
                raise RuntimeError(result["error"])

            text = result.get("response", "")

            if text:
                print(text, end="", flush=True)


def show_help():
    """Display available commands."""

    print(
        "\nCommands:\n"
        "  /help            Show available commands\n"
        "  /models          List installed Ollama models\n"
        "  /model NAME      Change the active model\n"
        "  /exit            Exit Open AI Toolkit\n"
    )


def main():
    """Run the interactive command-line interface."""

    current_model = DEFAULT_MODEL

    print("=" * 50)
    print("Open AI Toolkit")
    print("=" * 50)
    print(f"Active model: {current_model}")
    print("Type /help for available commands.\n")

    while True:
        try:
            prompt = input("You: ").strip()

            if not prompt:
                continue

            if prompt.lower() in {"/exit", "exit", "quit"}:
                print("Goodbye!")
                break

            if prompt == "/help":
                show_help()
                continue

            if prompt == "/models":
                models = list_models()

                if not models:
                    print("\nNo Ollama models are installed.\n")
                    continue

                print("\nInstalled models:")

                for model in models:
                    marker = "*" if model == current_model else "-"
                    print(f"  {marker} {model}")

                print()
                continue

            if prompt.startswith("/model "):
                new_model = prompt[7:].strip()

                if not new_model:
                    print("Usage: /model MODEL_NAME\n")
                    continue

                models = list_models()

                if new_model not in models:
                    print(
                        f"Model '{new_model}' is not installed.\n"
                        "Use /models to see available models.\n"
                    )
                    continue

                current_model = new_model
                print(f"Active model changed to: {current_model}\n")
                continue

            print(f"\n{current_model}: ", end="", flush=True)
            generate(prompt, current_model)
            print("\n")

        except RuntimeError as error:
            print(f"\nError: {error}\n")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()        for model in result.get("models", [])
    ]


def generate(prompt: str, model: str):
    """Generate and stream a response from Ollama."""

    data = {
        "model": model,
        "prompt": prompt,
        "stream": True,
    }

    with ollama_request("/api/generate", data) as response:
        for raw_line in response:
            if not raw_line:
                continue

            result = json.loads(raw_line.decode("utf-8"))

            if "error" in result:
                raise RuntimeError(result["error"])

            text = result.get("response", "")

            if text:
                print(text, end="", flush=True)


def show_help():
    """Display available commands."""

    print(
        "\nCommands:\n"
        "  /help            Show available commands\n"
        "  /models          List installed Ollama models\n"
        "  /model NAME      Change the active model\n"
        "  /exit            Exit Open AI Toolkit\n"
    )


def main():
    """Run the interactive command-line interface."""

    current_model = DEFAULT_MODEL

    print("=" * 50)
    print("Open AI Toolkit")
    print("=" * 50)
    print(f"Active model: {current_model}")
    print("Type /help for available commands.\n")

    while True:
        try:
            prompt = input("You: ").strip()

            if not prompt:
                continue

            if prompt.lower() in {"/exit", "exit", "quit"}:
                print("Goodbye!")
                break

            if prompt == "/help":
                show_help()
                continue

            if prompt == "/models":
                models = list_models()

                if not models:
                    print("\nNo Ollama models are installed.\n")
                    continue

                print("\nInstalled models:")

                for model in models:
                    marker = "*" if model == current_model else "-"
                    print(f"  {marker} {model}")

                print()
                continue

            if prompt.startswith("/model "):
                new_model = prompt[7:].strip()

                if not new_model:
                    print("Usage: /model MODEL_NAME\n")
                    continue

                models = list_models()

                if new_model not in models:
                    print(
                        f"Model '{new_model}' is not installed.\n"
                        "Use /models to see available models.\n"
                    )
                    continue

                current_model = new_model
                print(f"Active model changed to: {current_model}\n")
                continue

            print(f"\n{current_model}: ", end="", flush=True)
            generate(prompt, current_model)
            print("\n")

        except RuntimeError as error:
            print(f"\nError: {error}\n")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()            "Could not connect to Ollama. "
            "Make sure Ollama is installed and running."
        )


def main():
    print("Open AI Toolkit")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("You: ").strip()

        if prompt.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not prompt:
            continue

        response = generate(prompt)
        print(f"\nAI: {response}\n")


if __name__ == "__main__":
    main()
