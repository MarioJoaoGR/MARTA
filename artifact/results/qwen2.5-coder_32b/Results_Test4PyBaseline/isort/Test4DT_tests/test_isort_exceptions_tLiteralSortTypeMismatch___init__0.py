
# Test case  
# Module: isort.exceptions
import pytest
from isort.exceptions import LiteralSortTypeMismatch

def test_literal_sort_type_mismatch():
    # Test with int and list
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(int, list)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'list'> but was given a literal of type <class 'int'>."
    assert excinfo.value.kind is int
    assert excinfo.value.expected_kind is list

    # Test with str and float
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(str, float)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'float'> but was given a literal of type <class 'str'>."
    assert excinfo.value.kind is str
    assert excinfo.value.expected_kind is float

    # Test with dict and tuple
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(dict, tuple)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'tuple'> but was given a literal of type <class 'dict'>."
    assert excinfo.value.kind is dict
    assert excinfo.value.expected_kind is tuple

    # Test with custom types
    class CustomType1:
        pass

    class CustomType2:
        pass

    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(CustomType1, CustomType2)
    assert str(excinfo.value) == f"isort was told to sort a literal of type {CustomType2} but was given a literal of type {CustomType1}."
    assert excinfo.value.kind is CustomType1
    assert excinfo.value.expected_kind is CustomType2

    # Test with same types (should not raise)
    try:
        LiteralSortTypeMismatch(int, int)
    except LiteralSortTypeMismatch:
        pytest.fail("LiteralSortTypeMismatch should not be raised when kinds match")
