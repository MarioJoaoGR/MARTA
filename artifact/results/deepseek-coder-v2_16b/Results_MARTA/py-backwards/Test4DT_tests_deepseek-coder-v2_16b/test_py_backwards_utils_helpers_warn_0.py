
import pytest
from io import StringIO
import sys
from unittest.mock import patch
from py_backwards.utils.helpers import warn, messages

def test_valid_input():
    message = "This is a valid warning message."
    with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
        warn(message)
        assert mock_stderr.getvalue().strip() == messages.warn(message)

def test_none_input():
    with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
        warn(None)
        assert mock_stderr.getvalue().strip() == str(messages.warn(None))
