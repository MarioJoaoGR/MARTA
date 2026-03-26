
import pytest
from flutes.iterator import split_by

def test_invalid_input_missing_criterion_or_separator():
    iterable = [1, 2, 3]
    with pytest.raises(ValueError):
        list(split_by(iterable))
