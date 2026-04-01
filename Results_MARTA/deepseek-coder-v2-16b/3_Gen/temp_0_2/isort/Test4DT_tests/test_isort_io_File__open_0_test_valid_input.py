
from unittest.mock import patch, Mock
import pytest
from pathlib import Path
from io import TextIOWrapper
from isort.io import File

@pytest.fixture(autouse=True)
def mock_open():
    with patch('builtins.open', create=True) as mock_file:
        yield mock_file

def test_valid_input():
    # Mock the detect_encoding method to return a known encoding
    File.detect_encoding = Mock(return_value='utf-8')
    
    filename = Path("example_file.txt")
    expected_text = TextIOWrapper(open(str(filename), "rb"), encoding="utf-8", line_buffering=True, newline="")
    
    # Call the _open method with the mocked file object
    result = File._open(filename)
    
    assert isinstance(result, TextIOWrapper)
    assert result.mode == "r"
    assert result.encoding == "utf-8"
