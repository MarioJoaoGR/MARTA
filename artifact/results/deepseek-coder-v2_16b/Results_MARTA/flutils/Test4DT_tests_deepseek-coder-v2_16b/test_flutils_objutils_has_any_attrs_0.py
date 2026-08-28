
import pytest
from flutils.objutils import has_any_attrs



def test_has_callable_attributes():
    obj = {'get': lambda x: x, 'keys': lambda: None}
    attrs = ['get', 'keys']
    result = has_any_attrs(obj, *attrs)
    assert result is True, f"Expected True but got {result} for object with callable attributes."

def test_has_callable_and_non_callable_attributes():
    obj = {'get': lambda x: x, 'keys': None, 'items': lambda: None}
    attrs = ['get', 'keys', 'items']
    result = has_any_attrs(obj, *attrs)
    assert result is True, f"Expected True but got {result} for object with both callable and non-callable attributes."