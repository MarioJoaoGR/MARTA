
import pytest
from isort.exceptions import ISortError

def test_valid_case():
    with pytest.raises(ISortError):
        raise ISortError("An error occurred in isort")
