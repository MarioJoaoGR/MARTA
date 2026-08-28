
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_config import _EventSource


def test_handle_exceptions():
    event_source = _EventSource()

    def my_exception_handler(exc, *args, **kwargs):
        print(f"An exception occurred: {exc}")
        return False  # Return False to handle the exception internally

    event_source._handlers.add(my_exception_handler)

    with patch('sys.stdout', new=MagicMock()) as mock_stdout, \
         pytest.raises(ValueError):
        raise ValueError("Test exception")
        assert mock_stdout.getvalue().strip() == "An exception occurred: Test exception"

def test_fire_method():
    event_source = _EventSource()

    def my_exception_handler(exc, *args, **kwargs):
        print(f"An exception occurred: {exc}")
        return False  # Return False to handle the exception internally

    event_source._handlers.add(my_exception_handler)

    with patch('sys.stdout', new=MagicMock()) as mock_stdout, \
         pytest.raises(ValueError):
        raise ValueError("Test exception")
        assert mock_stdout.getvalue().strip() == "An exception occurred: Test exception"