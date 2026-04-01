
import pytest
from flutes.iterator import LazyList

def test_valid_case():
    lst = LazyList([1, 2, 3, 4])
    assert list(lst) == [1, 2, 3, 4]
    assert lst[0] == 1
    assert lst[2] == 3
    with pytest.raises(IndexError):
        lst[4]  # This should raise an IndexError as the list is not fully fetched yet
