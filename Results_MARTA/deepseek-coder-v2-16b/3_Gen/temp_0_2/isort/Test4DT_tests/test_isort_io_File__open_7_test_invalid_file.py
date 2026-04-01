
import pytest
from pathlib import Path
from io import TextIOWrapper
from unittest.mock import patch, mock_open

class File:
    @staticmethod
    def detect_encoding(filename: str | Path, first_line: bytes) -> str:
        # Mock implementation for testing purposes
        if b"invalid" in first_line:
            raise Exception("Unsupported encoding")
        return "utf-8"
    
    @staticmethod
    def _open(filename: str | Path) -> TextIOWrapper:
        """Open a file in read only mode using the encoding detected by
        detect_encoding().
        """
        buffer = open(filename, "rb")
        try:
            encoding = File.detect_encoding(filename, buffer.readline())
            buffer.seek(0)
            text = TextIOWrapper(buffer, encoding, line_buffering=True, newline="")
            text.mode = "r"  # type: ignore
            return text
        except Exception:
            buffer.close()
            raise

def test_invalid_file():
    with pytest.raises(Exception):
        File._open("nonexistent_file.txt")
