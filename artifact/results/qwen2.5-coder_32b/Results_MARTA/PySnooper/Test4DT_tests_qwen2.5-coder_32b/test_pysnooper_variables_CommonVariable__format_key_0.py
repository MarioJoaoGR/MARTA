
import pytest
from pysnooper.variables import CommonVariable

class MySubclass(CommonVariable):
    def __init__(self, source):
        super().__init__(source)

    def _format_key(self, key):
        return f"prefix_{key.upper()}"

class AnotherSubclass(CommonVariable):
    def __init__(self, source):
        super().__init__(source)

    def _format_key(self, key):
        return f"key_{key}_end"

def test_my_subclass_valid_key():
    my_var = MySubclass(source="test_source")
    formatted_key = my_var._format_key('example')
    assert formatted_key == 'prefix_EXAMPLE'

def test_another_subclass_valid_key():
    another_var = AnotherSubclass(source="test_source")
    formatted_key = another_var._format_key('test')
    assert formatted_key == 'key_test_end'

def test_common_variable_not_implemented_error():
    common_var = CommonVariable(source="test_source")
    with pytest.raises(NotImplementedError):
        common_var._format_key('some_key')


def test_another_subclass_none_key():
    another_var = AnotherSubclass(source="test_source")
    formatted_key = another_var._format_key(None)
    assert formatted_key == 'key_None_end'