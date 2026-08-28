
import pytest
from tornado.options import _Option

def test_invalid_inputs():
    with pytest.raises(ValueError):
        _Option(name="test_option", default=None, type=None)


