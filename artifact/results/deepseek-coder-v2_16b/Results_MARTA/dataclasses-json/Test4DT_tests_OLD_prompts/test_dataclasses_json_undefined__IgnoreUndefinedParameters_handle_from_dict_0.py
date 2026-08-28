
import pytest
from dataclasses_json.undefined import _IgnoreUndefinedParameters
from unittest.mock import patch, MagicMock

# Test scenario 1: handle_from_dict should return an empty dictionary when given an empty dictionary

# Test scenario 2: handle_from_dict should return the defined parameters from a given dictionary

# Test scenario 3: handle_from_dict should raise a TypeError if called with an instance instead of a class
def test_handle_from_dict_instance():
    class MyClass:
        def __init__(self, param1: int, param2: str):
            self.param1 = param1
            self.param2 = param2
    
    kvs = {'param1': 1, 'param2': 'test'}
    with pytest.raises(TypeError):
        known_params = _IgnoreUndefinedParameters.handle_from_dict(MyClass(**kvs), kvs)