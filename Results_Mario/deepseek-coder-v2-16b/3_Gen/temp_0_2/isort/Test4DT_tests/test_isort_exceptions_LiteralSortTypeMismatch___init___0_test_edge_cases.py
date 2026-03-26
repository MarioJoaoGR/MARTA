
import pytest
from isort.exceptions import LiteralSortTypeMismatch

def test_literal_sort_type_mismatch():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(str, int)
    
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'str'>."
