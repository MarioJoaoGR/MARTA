
import pytest
from types import SimpleNamespace
from flutils.namedtupleutils import _to_namedtuple as _  # Importing and aliasing the function correctly

# Test cases for the function _to_namedtuple
def test_basic_usage():
    obj = SimpleNamespace(a=1, b='test')
    result = _(obj)
    assert isinstance(result, tuple), "The result should be a named tuple"
    assert hasattr(result, 'a'), "The named tuple should have the attribute 'a'"
    assert hasattr(result, 'b'), "The named tuple should have the attribute 'b'"
    assert result.a == 1, "The attribute 'a' should be equal to 1"
    assert result.b == 'test', "The attribute 'b' should be equal to 'test'"

def test_unused_parameter():
    obj = SimpleNamespace(a=1, b='test')
    result = _(obj, _started=True)
    assert isinstance(result, tuple), "The result should be a named tuple"
    assert hasattr(result, 'a'), "The named tuple should have the attribute 'a'"
    assert hasattr(result, 'b'), "The named tuple should have the attribute 'b'"
    assert result.a == 1, "The attribute 'a' should be equal to 1"
    assert result.b == 'test', "The attribute 'b' should be equal to 'test'"

def test_different_data():
    obj = SimpleNamespace(x=10, y="example")
    result = _(obj)
    assert isinstance(result, tuple), "The result should be a named tuple"
    assert hasattr(result, 'x'), "The named tuple should have the attribute 'x'"
    assert hasattr(result, 'y'), "The named tuple should have the attribute 'y'"
    assert result.x == 10, "The attribute 'x' should be equal to 10"
    assert result.y == 'example', "The attribute 'y' should be equal to 'example'"
