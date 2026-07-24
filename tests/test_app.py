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
    def test_list_models(self, mock_request):
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

        models = app.list_models()

        self.assertEqual(
            models,
            ["llama3.2", "mistral"],
        )

        mock_request.assert_called_once_with("/api/tags")

    @patch("app.ollama_request")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_generate_streaming(self, mock_stdout, mock_request):
        """Streaming chunks should be printed in order."""

        chunks = [
            b'{"response":"Hello","done":false}\n',
            b'{"response":" world","done":false}\n',
            b'{"response":"!","done":true}\n',
        ]

        mock_response = MagicMock()
        mock_response.__iter__.return_value = iter(chunks)

        mock_request.return_value.__enter__.return_value = mock_response

        app.generate("Say hello", "llama3.2")

        self.assertEqual(
            mock_stdout.getvalue(),
            "Hello world!",
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
    def test_generate_handles_ollama_error(self, mock_request):
        """Errors returned by Ollama should raise RuntimeError."""

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
            app.generate("Hello", "missing-model")


if __name__ == "__main__":
    unittest.main()
