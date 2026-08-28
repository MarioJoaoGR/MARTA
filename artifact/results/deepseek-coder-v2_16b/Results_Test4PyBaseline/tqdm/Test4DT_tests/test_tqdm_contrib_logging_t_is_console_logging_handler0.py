# Module: tqdm.contrib.logging
import pytest
import logging
import sys
from tqdm.contrib.logging import _is_console_logging_handler

# Test cases for _is_console_logging_handler function
def test_is_console_logging_handler_stdout():
    handler = logging.StreamHandler(sys.stdout)
    assert _is_console_logging_handler(handler) is True

def test_is_console_logging_handler_stderr():
    handler = logging.StreamHandler(sys.stderr)
    assert _is_console_logging_handler(handler) is True

def test_is_console_logging_handler_not_stream_handler():
    class FakeHandler:
        pass
    fake_handler = FakeHandler()
    assert _is_console_logging_handler(fake_handler) is False

def test_is_console_logging_handler_wrong_stream():
    handler = logging.StreamHandler(open('test.log', 'w'))
    assert _is_console_logging_handler(handler) is False

if __name__ == "__main__":
    pytest.main()
