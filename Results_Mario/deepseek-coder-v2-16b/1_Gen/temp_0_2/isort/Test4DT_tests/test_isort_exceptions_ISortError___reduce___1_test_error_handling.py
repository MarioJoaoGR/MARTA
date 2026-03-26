
import pytest
from isort.exceptions import ISortError

def test_error_handling():
    with pytest.raises(ISortError):
        try:
            raise ISortError("Test exception for error handling")
        except ISortError as e:
            assert str(e) == "Test exception for error handling"
            raise  # Re-raise the exception to indicate failure if not caught correctly
