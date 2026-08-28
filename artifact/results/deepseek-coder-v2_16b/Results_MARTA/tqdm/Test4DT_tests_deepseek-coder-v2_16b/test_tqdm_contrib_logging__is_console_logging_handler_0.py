
import sys
import logging
from pytest import raises
from tqdm.contrib.logging import _is_console_logging_handler

def test_valid_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    assert _is_console_logging_handler(console_handler) is True

def test_invalid_handler():
    file_handler = logging.FileHandler('test.log')
    with raises(AssertionError):
        assert _is_console_logging_handler(file_handler)
