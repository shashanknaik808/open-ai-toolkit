"""
Open AI Toolkit

A lightweight toolkit for interacting with local AI models through Ollama.
"""

import json
import urllib.error
import urllib.request


OLLAMA_BASE_URL = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2"


def ollama_request(path, data=None):
    """Send a request to the local Ollama API."""

    url = f"{OLLAMA_BASE_URL}{path}"

    try:
        if data is None:
            return urllib.request.urlopen(url)

        request = urllib.request.Request(
            url,
            data=json.dumps(data).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
            },
            method="POST",
        )

        return urllib.request.urlopen(request)

    except urllib.error.HTTPError as error:
        raise RuntimeError(
            f"Ollama returned HTTP error {error.code}."
        ) from error

    except urllib.error.URLError as error:
        raise RuntimeError(
            "Could not connect to Ollama. "
            "Make sure Ollama is installed and running."
        ) from error


def get_models():
    """Return the names of locally installed Ollama models."""

    with ollama_request("/api/tags") as response:
        data = json.loads(
            response.read().decode("utf-8")
        )

    return [
        model["name"]
        for model in data.get("models", [])
        if "name" in model
    ]


def generate(prompt, model=DEFAULT_MODEL):
    """Generate a complete response from an Ollama model."""

    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }

    with ollama_request(
        "/api/generate",
        data,
    ) as response:
        result = json.loads(
            response.read().decode("utf-8")
        )

    if "error" in result:
        raise RuntimeError(result["error"])

    return result.get("response", "")


def generate_stream(prompt, model=DEFAULT_MODEL):
    """Stream response chunks from an Ollama model."""

    data = {
        "model": model,
        "prompt": prompt,
        "stream": True,
    }

    with ollama_request(
        "/api/generate",
        data,
    ) as response:

        for line in response:

            if not line:
                continue

            result = json.loads(
                line.decode("utf-8")
            )

            if "error" in result:
                raise RuntimeError(
                    result["error"]
                )

            chunk = result.get(
                "response",
                "",
            )

            if chunk:
                yield chunk

            if result.get(
                "done",
                False,
            ):
                break


def build_prompt(history, prompt):
    """Build a prompt containing conversation history."""

    lines = []

    for message in history:

        role = message.get(
            "role",
            "",
        )

        content = message.get(
            "content",
            "",
        )

        if role == "user":
            lines.append(
                f"User: {content}"
            )

        elif role == "assistant":
            lines.append(
                f"Assistant: {content}"
            )

    lines.append(
        f"User: {prompt}"
    )

    lines.append(
        "Assistant:"
    )

    return "\n".join(lines)


def choose_model():
    """Allow the user to choose an installed Ollama model."""

    try:
        models = get_models()

    except RuntimeError as error:
        print(
            f"\nError: {error}"
        )

        return DEFAULT_MODEL

    if not models:
        print(
            "\nNo Ollama models were found. "
            f"Using default model: {DEFAULT_MODEL}"
        )

        return DEFAULT_MODEL

    print("\nAvailable models:")

    for index, model in enumerate(
        models,
        start=1,
    ):
        print(
            f"{index}. {model}"
        )

    while True:

        choice = input(
            f"\nChoose a model [1-{len(models)}] "
            f"or press Enter for {models[0]}: "
        ).strip()

        if not choice:
            return models[0]

        try:
            index = int(choice) - 1

            if 0 <= index < len(models):
                return models[index]

        except ValueError:
            pass

        print(
            "Invalid selection. "
            "Please try again."
        )


def main():
    """Run the interactive Open AI Toolkit."""

    print("=" * 50)
    print("Open AI Toolkit")
    print("=" * 50)

    print(
        "\nLocal AI command-line interface "
        "powered by Ollama."
    )

    model = choose_model()

    print(
        f"\nUsing model: {model}"
    )

    print(
        "Type /model to change models."
    )

    print(
        "Type /stream to toggle streaming."
    )

    print(
        "Type /clear to clear conversation history."
    )

    print(
        "Type exit to quit."
    )

    streaming = True
    history = []

    while True:

        try:
            prompt = input(
                "\nYou: "
            ).strip()

        except (
            EOFError,
            KeyboardInterrupt,
        ):
            print(
                "\nGoodbye!"
            )
            break

        if not prompt:
            continue

        if prompt.lower() in {
            "exit",
            "quit",
        }:
            print(
                "Goodbye!"
            )
            break

        if prompt.lower() == "/model":

            model = choose_model()

            print(
                f"\nUsing model: {model}"
            )

            continue

        if prompt.lower() == "/stream":

            streaming = not streaming

            status = (
                "enabled"
                if streaming
                else "disabled"
            )

            print(
                f"\nStreaming {status}."
            )

            continue

        if prompt.lower() == "/clear":

            history.clear()

            print(
                "\nConversation history cleared."
            )

            continue

        full_prompt = build_prompt(
            history,
            prompt,
        )

        print(
            "\nAI: ",
            end="",
            flush=True,
        )

        try:

            if streaming:

                chunks = []

                for chunk in generate_stream(
                    full_prompt,
                    model,
                ):
                    print(
                        chunk,
                        end="",
                        flush=True,
                    )

                    chunks.append(
                        chunk
                    )

                response = "".join(
                    chunks
                )

                print()

            else:

                response = generate(
                    full_prompt,
                    model,
                )

                print(
                    response
                )

            history.append(
                {
                    "role": "user",
                    "content": prompt,
                }
            )

            history.append(
                {
                    "role": "assistant",
                    "content": response,
                }
            )

        except RuntimeError as error:

            print(
                f"\nError: {error}"
            )


if __name__ == "__main__":
    main()
