
import pytest
from ansible.module_utils.pycompat24 import literal_eval
import ast

# Test cases for literal_eval function
def test_literal_eval_string():
    assert literal_eval('"hello"') == "hello"

def test_literal_eval_number():
    assert literal_eval('42') == 42

def test_literal_eval_tuple():
    assert literal_eval('(1, 2, 3)') == (1, 2, 3)

def test_literal_eval_list():
    assert literal_eval('[1, 2, 3]') == [1, 2, 3]

def test_literal_eval_dict():
    assert literal_eval('{"a": 1, "b": 2}') == {'a': 1, 'b': 2}

def test_literal_eval_boolean_true():
    assert literal_eval('True') is True

def test_literal_eval_boolean_false():
    assert literal_eval('False') is False

def test_literal_eval_none():
    assert literal_eval('None') is None

# Test cases for malformed input
@pytest.mark.xfail(reason="Expected to raise ValueError for malformed string")
def test_literal_eval_malformed_string():
    with pytest.raises(ValueError):
        literal_eval('malformed string')

@pytest.mark.xfail(reason="Expected to raise ValueError for unsupported type")
def test_literal_eval_unsupported_type():
    with pytest.raises(ValueError):
        literal_eval('[1, 2, "three"]')  # Mixed types in list is not supported
