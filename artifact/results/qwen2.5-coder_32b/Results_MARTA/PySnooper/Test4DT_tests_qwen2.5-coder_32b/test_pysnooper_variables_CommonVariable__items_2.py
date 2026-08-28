
import pytest
from pysnooper.variables import CommonVariable

class MySubclass(CommonVariable):
    def __init__(self, source, unambiguous_source, exclude=[]):
        self.source = source
        self.unambiguous_source = unambiguous_source
        self.exclude = exclude

    def _keys(self, main_value):
        return iter(main_value.keys())
    
    def _get_value(self, main_value, key):
        return main_value[key]
    
    def _format_key(self, key):
        return f".{key}"

@pytest.fixture
def my_var():
    return MySubclass(source="MySource", unambiguous_source="UniqueSource:", exclude=['secret'])



def test_dictionary_input_without_normalize(my_var):
    data = {'name': 'Alice', 'age': 30, 'secret': 'hidden'}
    expected_output = [
        ('MySource', "{'name': 'Alice', 'age': 30, 'secret': 'hidden'}"),
        ('UniqueSource:.name', "'Alice'"),
        ('UniqueSource:.age', '30')
    ]
    result = my_var._items(data, normalize=False)
    assert result == expected_output


def test_string_input(my_var):
    data = "Hello, World!"
    expected_output = [
        ('MySource', "'Hello, World!'")
    ]
    result = my_var._items(data, normalize=False)
    assert result == expected_output