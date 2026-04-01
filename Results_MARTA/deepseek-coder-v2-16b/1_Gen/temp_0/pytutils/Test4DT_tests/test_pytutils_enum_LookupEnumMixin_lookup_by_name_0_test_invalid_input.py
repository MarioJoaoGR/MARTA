
import pytest
from pytutils.enum import LookupEnumMixin
from enum import Enum

def test_invalid_input():
    class InvalidEnum(Enum):  # Create an invalid enum for testing
        VALID = 1
    
    with pytest.raises(AttributeError):
        LookupEnumMixin.lookup_by_name(InvalidEnum)
