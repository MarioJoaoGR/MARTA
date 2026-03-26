# Module: isort.exceptions
import pytest

from isort.exceptions import LiteralSortTypeMismatch


def test_literal_sort_type_mismatch():
    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(str, int)
    
    assert str(exc_info.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'str'>."

def test_literal_sort_type_mismatch_with_different_types():
    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(list, dict)
    
    assert str(exc_info.value) == "isort was told to sort a literal of type <class 'dict'> but was given a literal of type <class 'list'>."
