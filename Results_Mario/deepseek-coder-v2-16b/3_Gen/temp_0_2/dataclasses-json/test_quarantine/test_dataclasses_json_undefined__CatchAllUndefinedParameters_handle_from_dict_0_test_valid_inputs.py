
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from unittest.mock import patch, MagicMock
from dataclasses_json.undefined import handle_from_dict, UndefinedParameterError

@dataclass
class ExampleClass:
    field1: int
    field2: str

def test_valid_inputs():
    kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
    
    with patch('dataclasses_json.undefined._UndefinedParameterAction._separate_defined_undefined_kvs') as mock_separate:
        mock_separate.return_value = ({'extra_param': 'value'}, {'extra_param': 'value'})
        
        known_params = handle_from_dict(ExampleClass, kvs)
        
        assert known_params == {'field1': 1, 'field2': 'hello', 'extra_param': 'value'}

def test_invalid_input():
    kvs = {'catch_all_field': {}}
    
    with patch('dataclasses_json.undefined._CatchAllUndefinedParameters._get_catch_all_field') as mock_get_catch_all:
        catch_all_field = MagicMock()
        mock_get_catch_all.return_value = catch_all_field
        
        with patch('dataclasses_json.undefined._CatchAllUndefinedParameters._get_default') as mock_get_default:
            default_value = {}
            mock_get_default.return_value = default_value
            
            with pytest.raises(UndefinedParameterError):
                handle_from_dict(ExampleClass, kvs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_valid_inputs.py:6:0: E0611: No name 'handle_from_dict' in module 'dataclasses_json.undefined' (no-name-in-module)


"""