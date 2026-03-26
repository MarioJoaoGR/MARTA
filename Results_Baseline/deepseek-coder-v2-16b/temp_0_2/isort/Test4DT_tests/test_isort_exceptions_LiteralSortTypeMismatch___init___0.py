
import pytest

from isort.exceptions import LiteralSortTypeMismatch


# Test cases for the LiteralSortTypeMismatch class
def test_literal_sort_type_mismatch():
    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(str, int)
    assert str(exc_info.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'str'>."

def test_literal_sort_type_mismatch_different_types():
    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(float, int)
    assert str(exc_info.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'float'>."

def test_literal_sort_type_mismatch_user_defined_types():
    class MyCustomType:
        pass
    
    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(MyCustomType, list)