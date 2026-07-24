"""Tests for Open AI Toolkit."""

import io
import json
import unittest
from unittest.mock import MagicMock, patch

import app


class TestOpenAIToolkit(unittest.TestCase):

    def test_default_model(self):
        """The default model should be llama3.2."""
        self.assertEqual(app.DEFAULT_MODEL, "llama3.2")

    @patch("app.ollama_request")
    def test_get_models(self, mock_request):
        """Installed Ollama models should be returned correctly."""

        response_data = {
            "models": [
                {"name": "llama3.2"},
                {"name": "mistral"},
            ]
        }

        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(
            response_data
        ).encode("utf-8")

        mock_request.return_value.__enter__.return_value = mock_response

        models = app.get_models()

        self.assertEqual(
            models,
            ["llama3.2", "mistral"],
        )

        mock_request.assert_called_once_with(
            "/api/tags"
        )

    @patch("app.ollama_request")
    def test_generate(self, mock_request):
        """Non-streaming generation should return the response."""

        response_data = {
            "response": "Hello world!"
        }

        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(
            response_data
        ).encode("utf-8")

        mock_request.return_value.__enter__.return_value = mock_response

        result = app.generate(
            "Say hello",
            "llama3.2",
        )

        self.assertEqual(
            result,
            "Hello world!",
        )

        mock_request.assert_called_once_with(
            "/api/generate",
            {
                "model": "llama3.2",
                "prompt": "Say hello",
                "stream": False,
            },
        )

    @patch("app.ollama_request")
    def test_generate_streaming(self, mock_request):
        """Streaming chunks should be returned in order."""

        chunks = [
            b'{"response":"Hello","done":false}\n',
            b'{"response":" world","done":false}\n',
            b'{"response":"!","done":true}\n',
        ]

        mock_response = MagicMock()
        mock_response.__iter__.return_value = iter(chunks)

        mock_request.return_value.__enter__.return_value = mock_response

        result = list(
            app.generate_stream(
                "Say hello",
                "llama3.2",
            )
        )

        self.assertEqual(
            result,
            [
                "Hello",
                " world",
                "!",
            ],
        )

        mock_request.assert_called_once_with(
            "/api/generate",
            {
                "model": "llama3.2",
                "prompt": "Say hello",
                "stream": True,
            },
        )

    @patch("app.ollama_request")
    def test_generate_handles_ollama_error(
        self,
        mock_request,
    ):
        """Ollama errors should raise RuntimeError."""

        chunks = [
            b'{"error":"model not found"}\n',
        ]

        mock_response = MagicMock()
        mock_response.__iter__.return_value = iter(chunks)

        mock_request.return_value.__enter__.return_value = mock_response

        with self.assertRaisesRegex(
            RuntimeError,
            "model not found",
        ):
            list(
                app.generate_stream(
                    "Hello",
                    "missing-model",
                )
            )

    def test_build_prompt_without_history(self):
        """A new conversation should contain the current prompt."""

        result = app.build_prompt(
            [],
            "Hello",
        )

        self.assertEqual(
            result,
            "User: Hello\nAssistant:",
        )

    def test_build_prompt_with_history(self):
        """Previous messages should be included in the prompt."""

        history = [
            {
                "role": "user",
                "content": "My name is Shashank.",
            },
            {
                "role": "assistant",
                "content": "Nice to meet you, Shashank.",
            },
        ]

        result = app.build_prompt(
            history,
            "What is my name?",
        )

        expected = (
            "User: My name is Shashank.\n"
            "Assistant: Nice to meet you, Shashank.\n"
            "User: What is my name?\n"
            "Assistant:"
        )

        self.assertEqual(
            result,
            expected,
        )

    def test_build_prompt_multiple_messages(self):
        """Conversation history should preserve message order."""

        history = [
            {
                "role": "user",
                "content": "First question",
            },
            {
                "role": "assistant",
                "content": "First answer",
            },
            {
                "role": "user",
                "content": "Second question",
            },
            {
                "role": "assistant",
                "content": "Second answer",
            },
        ]

        result = app.build_prompt(
            history,
            "Third question",
        )

        self.assertIn(
            "User: First question",
            result,
        )

        self.assertIn(
            "Assistant: First answer",
            result,
        )

        self.assertIn(
            "User: Second question",
            result,
        )

        self.assertIn(
            "Assistant: Second answer",
            result,
        )

        self.assertTrue(
            result.endswith(
                "User: Third question\nAssistant:"
            )
        )


if __name__ == "__main__":
    unittest.main()
