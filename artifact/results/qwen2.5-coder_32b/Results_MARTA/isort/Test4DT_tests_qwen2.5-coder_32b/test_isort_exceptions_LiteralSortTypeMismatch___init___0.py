
import pytest
from isort.exceptions import LiteralSortTypeMismatch

def test_edge_case_none():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(type(None), str)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'str'> but was given a literal of type <class 'NoneType'>."

def test_edge_case_int_str():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(int, str)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'str'> but was given a literal of type <class 'int'>."

def test_edge_case_list_tuple():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(list, tuple)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'tuple'> but was given a literal of type <class 'list'>."

def test_edge_case_float_int():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(float, int)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'float'>."

def test_edge_case_dict_set():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(dict, set)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'set'> but was given a literal of type <class 'dict'>."
