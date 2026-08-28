
import pytest
from pysnooper.variables import CommonVariable

class MyVariable(CommonVariable):
    def _get_value(self, main_value, key):
        return main_value.get(key)

class MyListVariable(CommonVariable):
    def _get_value(self, main_value, key):
        try:
            return main_value[key]
        except IndexError:
            return None

class MyObjectVariable(CommonVariable):
    def _get_value(self, main_value, key):
        return getattr(main_value, key, None)

class SampleObject:
    def __init__(self):
        self.x = 100
        self.y = 200

def test_my_variable_dict():
    my_var = MyVariable(source="{}")  # Initialize with a valid source string
    assert my_var._get_value({'a': 1, 'b': 2}, 'a') == 1
    assert my_var._get_value({'a': 1, 'b': 2}, 'c') is None

def test_my_list_variable():
    my_list_var = MyListVariable(source="[]")  # Initialize with a valid source string
    assert my_list_var._get_value([10, 20, 30], 0) == 10
    assert my_list_var._get_value([10, 20, 30], 5) is None

def test_my_object_variable():
    my_object_var = MyObjectVariable(source="SampleObject()")  # Initialize with a valid source string
    sample_obj = SampleObject()
    assert my_object_var._get_value(sample_obj, 'x') == 100
    assert my_object_var._get_value(sample_obj, 'z') is None

def test_common_variable_not_implemented():
    common_var = CommonVariable(source="{}")  # Initialize with a valid source string
    with pytest.raises(NotImplementedError):
        common_var._get_value({}, 'key')
