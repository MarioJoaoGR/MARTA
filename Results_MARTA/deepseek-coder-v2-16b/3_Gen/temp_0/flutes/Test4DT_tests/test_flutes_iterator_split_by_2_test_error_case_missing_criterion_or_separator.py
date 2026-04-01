
import pytest
from flutes.iterator import split_by

def test_error_case_missing_criterion_or_separator():
    iterable = range(5)
    with pytest.raises(ValueError):
        list(split_by(iterable))
