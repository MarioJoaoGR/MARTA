
import pytest
from pytutils.enum import LookupEnumMixin

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

def test_none_input():
    with pytest.raises(TypeError):
        ExampleEnum.lookup_by_any(None)
