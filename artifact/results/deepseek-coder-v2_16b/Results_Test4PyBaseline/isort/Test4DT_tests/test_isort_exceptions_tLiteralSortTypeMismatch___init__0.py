# Module: isort.exceptions
import pytest
from isort.exceptions import LiteralSortTypeMismatch

# Test cases for the LiteralSortTypeMismatch exception
def test_literal_sort_type_mismatch():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(str, int)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'str'>."

def test_literal_sort_type_mismatch_different_types():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(float, int)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'float'>."

def test_literal_sort_type_mismatch_builtin_types():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(str, str)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'str'> but was given a literal of type <class 'str'>."
