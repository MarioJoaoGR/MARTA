
import pytest
from apimd.parser import _type_name


def test_type_name_with_builtin_type():
    num = 42
    type_name = _type_name(num)
    assert type_name == 'int'

def test_type_name_with_custom_object():
    import math
    value = math.sqrt(9)
    type_name = _type_name(value)
    assert type_name == 'float'