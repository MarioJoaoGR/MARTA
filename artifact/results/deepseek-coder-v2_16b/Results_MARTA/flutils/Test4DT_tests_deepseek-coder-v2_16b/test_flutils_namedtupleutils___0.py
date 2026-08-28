
import pytest
from types import SimpleNamespace
from flutils.namedtupleutils import _to_namedtuple
from collections import namedtuple, OrderedDict
from typing import Union, Any, Mapping, List, Tuple

def test_valid_case_1():
    ns = SimpleNamespace(a=1, b='test')
    result = _to_namedtuple(ns)
    assert isinstance(result, tuple), f"Expected a tuple but got {type(result)}"
    assert hasattr(result, 'a'), "Expected attribute 'a' in the namedtuple"
    assert hasattr(result, 'b'), "Expected attribute 'b' in the namedtuple"
    assert getattr(result, 'a') == 1, f"Expected value for 'a' to be 1 but got {getattr(result, 'a')}"
    assert getattr(result, 'b') == 'test', f"Expected value for 'b' to be 'test' but got {getattr(result, 'b')}"

def test_valid_case_2():
    ns = SimpleNamespace(x=42, y='example')
    result = _to_namedtuple(ns)
    assert isinstance(result, tuple), f"Expected a tuple but got {type(result)}"
    assert hasattr(result, 'x'), "Expected attribute 'x' in the namedtuple"
    assert hasattr(result, 'y'), "Expected attribute 'y' in the namedtuple"
    assert getattr(result, 'x') == 42, f"Expected value for 'x' to be 42 but got {getattr(result, 'x')}"
    assert getattr(result, 'y') == 'example', f"Expected value for 'y' to be 'example' but got {getattr(result, 'y')}"

def test_valid_case_3():
    ns = SimpleNamespace(c=3.14, d='string')
    result = _to_namedtuple(ns)
    assert isinstance(result, tuple), f"Expected a tuple but got {type(result)}"
    assert hasattr(result, 'c'), "Expected attribute 'c' in the namedtuple"
    assert hasattr(result, 'd'), "Expected attribute 'd' in the namedtuple"
    assert getattr(result, 'c') == 3.14, f"Expected value for 'c' to be 3.14 but got {getattr(result, 'c')}"
    assert getattr(result, 'd') == 'string', f"Expected value for 'd' to be 'string' but got {getattr(result, 'd')}"

def test_error_case_invalid_input():
    ns = 12345
    with pytest.raises(TypeError):
        _to_namedtuple(ns)
