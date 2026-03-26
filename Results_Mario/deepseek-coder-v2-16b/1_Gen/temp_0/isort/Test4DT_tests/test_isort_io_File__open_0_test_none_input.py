
import pytest
from pathlib import Path
from io import TextIOWrapper
from unittest.mock import patch, MagicMock

class File:
    @staticmethod
    def detect_encoding(filename: str | Path, first_line: bytes) -> str:
        # Mock implementation for detecting encoding
        return "utf-8"
    
    @staticmethod
    def _open(filename: str | Path) -> TextIOWrapper:
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

def test_none_input():
    with pytest.raises(Exception):
        File._open(None)
