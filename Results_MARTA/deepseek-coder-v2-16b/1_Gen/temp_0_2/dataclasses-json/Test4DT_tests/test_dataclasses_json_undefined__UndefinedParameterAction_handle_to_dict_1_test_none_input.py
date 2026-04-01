
from dataclasses_json import undefined
import pytest

class _UndefinedParameterAction:
    def handle_to_dict(self, obj, kvs: dict) -> dict:
        """
        Return the parameters that will be written to the output dict
        """
        return kvs

def test_none_input():
    action = _UndefinedParameterAction()
    result = action.handle_to_dict(None, {'key1': 'value1', 'key2': 'value2'})
    assert result == {'key1': 'value1', 'key2': 'value2'}
