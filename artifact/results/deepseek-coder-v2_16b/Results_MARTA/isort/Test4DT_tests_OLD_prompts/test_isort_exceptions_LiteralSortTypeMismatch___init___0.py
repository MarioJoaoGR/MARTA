
import pytest
from isort.exceptions import LiteralSortTypeMismatch

# Test valid input scenario where the expected type matches the provided literal

# Test invalid input scenario where the provided literal does not match the expected type
def test_invalid_input():
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        sort_literal("incorrect_type")  # This would raise an error since "incorrect_type" is not the expected type
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'list'> but was given a literal of type <class 'str'>."

# Mock function for testing purposes
def sort_literal(data):
    if not isinstance(data, list):
        raise LiteralSortTypeMismatch(type(data), list)