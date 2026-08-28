
import pytest
from flutes.iterator import take

def test_valid_case():
    result = list(take(5, range(1000000)))
    assert result == [0, 1, 2, 3, 4]

def test_edge_case():
    result = list(take(0, range(10)))
    assert result == []

def test_error_case():
    with pytest.raises(ValueError) as e:
        result = list(take(-1, range(1000000)))
    assert str(e.value) == "`n` should be non-negative"
