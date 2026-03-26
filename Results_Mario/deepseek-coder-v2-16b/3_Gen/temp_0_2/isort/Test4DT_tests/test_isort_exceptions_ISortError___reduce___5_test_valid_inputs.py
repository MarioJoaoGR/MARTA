
import pytest
from isort.exceptions import ISortError

def test_valid_inputs():
    # Test creating an instance of ISortError and verifying its type
    try:
        raise ISortError("This is a test error message")
    except ISortError as e:
        assert isinstance(e, ISortError)
        assert str(e) == "This is a test error message"
