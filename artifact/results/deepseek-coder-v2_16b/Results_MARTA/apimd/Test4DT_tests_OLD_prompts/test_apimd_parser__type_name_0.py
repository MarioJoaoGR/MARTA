
import pytest
from apimd.parser import _type_name


def test_builtin_type():
    num = 42
    assert _type_name(num) == 'int'

def test_module_object():
    import math
    value = math.sqrt(9)
    assert _type_name(value) == 'float'