
import pytest
from isort.exceptions import LiteralSortTypeMismatch

def test_valid_inputs():
    with pytest.raises(LiteralSortTypeMismatch) as exc_info:
        raise LiteralSortTypeMismatch(str, int)
    assert str(exc_info.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'str'>."
