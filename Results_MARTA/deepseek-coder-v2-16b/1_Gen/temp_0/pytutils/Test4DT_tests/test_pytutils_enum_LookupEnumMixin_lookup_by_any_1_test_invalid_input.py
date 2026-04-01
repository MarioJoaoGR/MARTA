
import pytest
from pytutils.enum import LookupEnumMixin

# Define a sample enum class with the mixin
class ExampleEnum(LookupEnumMixin):
    A = 1
    B = 2

    lookup_by_name = {
        'A': 1,
        'B': 2
    }
    lookup_by_value = {
        1: 'A',
        2: 'B'
    }

# Test function for invalid input type
def test_invalid_input():
    with pytest.raises(TypeError):
        ExampleEnum.lookup_by_any("invalid_input")
