
import pytest
import sys
from ansible.module_utils.pycompat24 import get_exception

def test_get_exception_no_error():
    try:
        # Code that might raise an exception
        1 / 0
    except Exception as e:
        result = get_exception()
        assert isinstance(result, type(e))
        assert str(result) == str(e)
    else:
        pytest.fail("Expected an exception but none was raised")

def test_get_exception_no_error_without_triggering():
    result = get_exception()
    assert result is None
