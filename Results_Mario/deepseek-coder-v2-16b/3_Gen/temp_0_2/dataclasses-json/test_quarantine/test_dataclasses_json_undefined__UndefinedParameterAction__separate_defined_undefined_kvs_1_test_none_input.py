
from dataclasses import fields
from typing import Dict, Tuple
import pytest
from dataclasses_json.undefined import UndefinedParameterAction  # Importing from the correct module

class ExampleClass:
    field1: int
    field2: str

def test_none_input():
    kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
    
    known, unknown = _separate_defined_undefined_kvs(ExampleClass, kvs)
    
    assert isinstance(known, dict)
    assert isinstance(unknown, dict)
    assert len(known) == 2
    assert len(unknown) == 1
    assert 'field1' in known
    assert 'field2' in known
    assert 'extra_param' in unknown
    assert known['field1'] == 1
    assert known['field2'] == 'hello'
    assert unknown['extra_param'] == 'value'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_1_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_1_test_none_input.py:5:0: E0611: No name 'UndefinedParameterAction' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_1_test_none_input.py:14:21: E0602: Undefined variable '_separate_defined_undefined_kvs' (undefined-variable)


"""