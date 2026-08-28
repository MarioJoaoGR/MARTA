
from tornado.util import ObjectDict
import pytest

def test_invalid_input():
    obj = ObjectDict()
    with pytest.raises(AttributeError):
        obj.nonexistent_attribute  # This should raise a TypeError because the attribute does not exist
