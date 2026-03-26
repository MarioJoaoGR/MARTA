
import pytest
from dataclasses_json.utils import _get_type_cons

def test_none_input():
    with pytest.raises(AttributeError):
        result = _get_type_cons(None)
