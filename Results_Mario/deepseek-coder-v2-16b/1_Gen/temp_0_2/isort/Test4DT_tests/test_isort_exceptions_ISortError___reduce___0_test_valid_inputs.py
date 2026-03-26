
import pytest
from isort.exceptions import ISortError

def test_valid_inputs():
    with pytest.raises(ISortError):
        raise ISortError("This is a test error to ensure the exception behaves as expected.")
