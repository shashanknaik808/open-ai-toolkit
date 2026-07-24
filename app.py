"""
Open AI Toolkit
A lightweight toolkit for interacting with local AI models.
"""

import json
import urllib.request
import urllib.error


OLLAMA_URL = "http://localhost:11434/api/generate"


def generate(prompt: str, model: str = "llama3.2") -> str:
    """Send a prompt to a locally running Ollama model."""

    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }

    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["response"]

    except urllib.error.URLError:
        return (
            "Could not connect to Ollama. "
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
