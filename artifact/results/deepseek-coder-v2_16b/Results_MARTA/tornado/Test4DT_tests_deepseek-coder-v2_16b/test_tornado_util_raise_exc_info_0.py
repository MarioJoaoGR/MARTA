
import pytest
from tornado.util import raise_exc_info
import sys

def test_raise_exc_info_with_exception():
    try:
        1 / 0
    except Exception as e:
        exc_info = sys.exc_info()
        with pytest.raises(Exception) as exc_info_context:
            raise_exc_info(exc_info)
        assert str(exc_info_context.value) == str(e)

def test_raise_exc_info_without_exception():
    exc_info = (None, None, None)
    with pytest.raises(TypeError) as exc_info_context:
        raise_exc_info(exc_info)
    assert str(exc_info_context.value) == "raise_exc_info called with no exception"
