
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from isort.io import \
    File  # Assuming this module exists and contains the File class definition


@pytest.fixture
def valid_file():
    content = ["line1", "line2", "line3"]
    mock_stream = MagicMock()
    mock_stream.__iter__.return_value = iter(content)  # Mock iteration over lines
    with patch('builtins.open', create=True):  # Create a context for mocking open function
        yield File(stream=mock_stream, path="fakepath", encoding="utf-8")

def test_invalid_file():
    with pytest.raises(Exception):
        list(File.read("nonexistentfile.txt"))
