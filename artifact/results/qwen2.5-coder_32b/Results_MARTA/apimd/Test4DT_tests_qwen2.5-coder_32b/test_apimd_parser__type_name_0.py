
import pytest
from apimd.parser import _type_name

# Test for built-in integer type
def test_type_name_int():
    obj = 123
    assert _type_name(obj) == 'int'

# Test for built-in list type
def test_type_name_list():
    obj = [1, 2, 3]
    assert _type_name(obj) == 'list'

# Test for built-in string type
def test_type_name_str():
    obj = "Hello"
    assert _type_name(obj) == 'str'

# Test for custom class instance

# Test for built-in dictionary type
def test_type_name_dict():
    obj = {'key': 'value'}
    assert _type_name(obj) == 'dict'

# Test for built-in float type
def test_type_name_float():
    obj = 3.14
    assert _type_name(obj) == 'float'