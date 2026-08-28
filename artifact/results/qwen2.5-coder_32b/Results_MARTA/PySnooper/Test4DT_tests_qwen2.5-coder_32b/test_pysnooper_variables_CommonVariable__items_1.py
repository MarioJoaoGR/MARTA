
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
        return f".{key}"

def test_dictionary_with_invalid_value():
    my_var = MySubclass(source='MySource', unambiguous_source='UniqueSource:', exclude=[])
    data6 = {'invalid_key': object()}
    expected_output_data6 = [
        ('MySource', "{'invalid_key': <object object at ...>}"),
        ('UniqueSource:.invalid_key', "<object object at ...>")
    ]
    result_data6 = my_var._items(data6, normalize=False)
    assert len(result_data6) == 2
    assert result_data6[0][0] == expected_output_data6[0][0]
    assert 'object at' in result_data6[0][1]
    assert result_data6[1][0] == expected_output_data6[1][0]
    assert 'object at' in result_data6[1][1]


def test_list_input():
    my_var = MySubclass(source='MySource', unambiguous_source='UniqueSource:', exclude=[])
    data2 = [1, 2, 3]
    expected_output = [
        ('MySource', '[1, 2, 3]'),
        ('UniqueSource:[0]', '1'),
        ('UniqueSource:[1]', '2'),
        ('UniqueSource:[2]', '3')
    ]
    result = my_var._items(data2, normalize=False)
    assert len(result) == 4
    assert result[0] == expected_output[0]
    assert result[1] == expected_output[1]
    assert result[2] == expected_output[2]
    assert result[3] == expected_output[3]

def test_string_input():
    my_var = MySubclass(source='MySource', unambiguous_source='UniqueSource:', exclude=[])
    data3 = "Hello, World!"
    expected_output = [
        ('MySource', "'Hello, World!'")
    ]
    result = my_var._items(data3, normalize=False)
    assert len(result) == 1
    assert result[0] == expected_output[0]