
import pytest
from pysnooper.variables import CommonVariable

class MySubclass(CommonVariable):
    def __init__(self, source, unambiguous_source, exclude=[]):
        self.source = source
        self.unambiguous_source = unambiguous_source
        self.exclude = exclude

    def _keys(self, main_value):
        if isinstance(main_value, dict):
            return iter(main_value.keys())
        elif isinstance(main_value, list):
            return iter(range(len(main_value)))
        else:
            return []

    def _get_value(self, main_value, key):
        return main_value[key]

    def _format_key(self, key):
        if isinstance(key, int):
            return f"[{key}]"
        else:
            return f".{key}"


def test_happy_path_dict_no_normalize():
    my_var = MySubclass(source='MySource', unambiguous_source='UniqueSource:', exclude=['secret'])
    data = {'name': 'Alice', 'age': 30, 'secret': 'hidden'}
    expected_output = [
        ('MySource', "{'name': 'Alice', 'age': 30, 'secret': 'hidden'}"),
        ('UniqueSource:.name', "'Alice'"),
        ('UniqueSource:.age', '30')
    ]
    assert my_var._items(data, normalize=False) == expected_output

def test_happy_path_list():
    my_var = MySubclass(source='MySource', unambiguous_source='UniqueSource:', exclude=[])
    data = [1, 2, 3]
    expected_output = [
        ('MySource', '[1, 2, 3]'),
        ('UniqueSource:[0]', '1'),
        ('UniqueSource:[1]', '2'),
        ('UniqueSource:[2]', '3')
    ]
    assert my_var._items(data) == expected_output

def test_happy_path_string():
    my_var = MySubclass(source='MySource', unambiguous_source='UniqueSource:', exclude=[])
    data = "Hello, World!"
    expected_output = [
        ('MySource', "'Hello, World!'")
    ]
    assert my_var._items(data) == expected_output