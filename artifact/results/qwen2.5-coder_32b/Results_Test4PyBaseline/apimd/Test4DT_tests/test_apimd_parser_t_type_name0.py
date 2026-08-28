
# Test case  
import pytest
from apimd.parser import _type_name

def test_type_name_builtin_types():
    assert _type_name(123) == 'int'
    assert _type_name([1, 2, 3]) == 'list'
    assert _type_name("Hello") == 'str'
    assert _type_name(3.14) == 'float'

def test_type_name_user_defined_class():
    class MyClass:
        pass
    obj = MyClass()
    assert _type_name(obj).endswith('.MyClass')

def test_type_name_function():
    def my_function():
        pass