
from io import TextIOWrapper
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

import isort.io


class File:
    @staticmethod
    def _open(filename: str | Path) -> TextIOWrapper:
        """Open a file in read only mode using the encoding detected by
        detect_encoding().
        """
        buffer = open(filename, "rb")
        try:
            encoding = File.detect_encoding(filename, buffer.readline)
            buffer.seek(0)
            text = TextIOWrapper(buffer, encoding, line_buffering=True, newline="")
            text.mode = "r"  # type: ignore
            return text
        except Exception:
            buffer.close()
            raise
    
    @staticmethod
    def detect_encoding(filename: str | Path, first_line: callable) -> str:
        """Detect the encoding of a file based on its first line."""
        # This is a mock implementation for testing purposes
        return "utf-8"

def test_none_input():
    with pytest.raises(TypeError):
        File._open(None)
