
import pytest
from isort.exceptions import ISortError

def test_error_handling():
    with pytest.raises(ISortError):
        raise ISortError("An error occurred in isort")
