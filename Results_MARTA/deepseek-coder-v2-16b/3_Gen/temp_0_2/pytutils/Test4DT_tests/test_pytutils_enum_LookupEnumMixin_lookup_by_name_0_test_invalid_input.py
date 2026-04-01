
import pytest
from pytutils.enum import LookupEnumMixin

# Define a mock InvalidType class for testing invalid input
class InvalidType:
    pass

def test_invalid_input():
    with pytest.raises(AttributeError):
        LookupEnumMixin.lookup_by_name(InvalidType)
