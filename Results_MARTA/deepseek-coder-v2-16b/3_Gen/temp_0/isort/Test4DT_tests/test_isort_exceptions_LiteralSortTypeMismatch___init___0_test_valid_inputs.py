
import pytest

from isort.exceptions import LiteralSortTypeMismatch


def test_valid_inputs():
    # Test case where kind and expected_kind are of different types
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(str, int)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'str'>."

    # Test case where kind and expected_kind are the same type
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(list, list)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'list'> but was given a literal of type <class 'list'>."
