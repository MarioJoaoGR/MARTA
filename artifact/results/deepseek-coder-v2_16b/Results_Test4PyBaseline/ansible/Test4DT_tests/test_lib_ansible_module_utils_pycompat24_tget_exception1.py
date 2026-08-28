
import pytest
import sys
from ansible.module_utils.pycompat24 import get_exception

def test_get_exception_no_error():
    try:
        # Code that might raise an exception
        1 / 0
    except Exception as e:
        assert isinstance(get_exception(), Exception), f"Expected {type(e)} but got {type(get_exception())}"
        assert str(e) == str(get_exception()), f"Expected '{str(e)}' but got '{str(get_exception())}'"

def test_get_exception_with_error():
    try:
        # Another code that might raise an exception
        int("not a number")
    except Exception as e:
        assert isinstance(get_exception(), Exception), f"Expected {type(e)} but got {type(get_exception())}"
        assert str(e) == str(get_exception()), f"Expected '{str(e)}' but got '{str(get_exception())}'"

def test_get_exception_no_current_exception():
    # Clear the current exception to simulate no active exception
    sys.exc_info = (None, None, None)
    with pytest.raises(Exception):
        get_exception()
