
import pytest
import logging
from unittest.mock import patch, MagicMock
from tqdm.contrib.logging import _is_console_logging_handler

# Test for valid console logging handler
def test_valid_input():
    with patch('sys.stdout', new=MagicMock()) as mock_stdout:
        console_handler = logging.StreamHandler(mock_stdout)
        result = _is_console_logging_handler(console_handler)
        assert result is True, "Expected True for a valid console logging handler"

# Test for invalid input (None type)
def test_invalid_input():
    none_handler = None
    result = _is_console_logging_handler(none_handler)
    assert result is False, "Expected False for an invalid input"

# Test for a handler that is not a StreamHandler
def test_not_a_stream_handler():
    file_handler = logging.FileHandler('test.log')
    result = _is_console_logging_handler(file_handler)
    assert result is False, "Expected False for a non-StreamHandler type"
