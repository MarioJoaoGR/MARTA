# Module: tornado.util
import pytest
import sys
from types import TracebackType
from typing import Optional, Tuple

# Import the function correctly
from tornado.util import raise_exc_info

def test_raise_exc_info_with_exception():
    try:
        1 / 0
    except Exception as e:
        exc_info = sys.exc_info()
        with pytest.raises(ZeroDivisionError):
            raise_exc_info(exc_info)

def test_raise_exc_info_without_exception():
    exc_info = (None, None, None)
    with pytest.raises(TypeError):
        raise_exc_info(exc_info)

def test_raise_exc_info_with_specific_caught_exception():
    try:
        int("not_a_number")
    except ValueError as e:
        exc_info = sys.exc_info()
        with pytest.raises(ValueError):
            raise_exc_info(exc_info)
