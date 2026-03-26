
# Module: dataclasses_json.undefined
import pytest
from dataclasses import dataclass
from typing import Dict, Tuple, List
from dataclasses_json import undefined

# Import the function from the module
_separate_defined_undefined_kvs = undefined._separate_defined_undefined_kvs

@dataclass
class TestClass:
    param1: int
    param2: str

def test_separate_defined_undefined_kvs():
    # Create a sample class with fields
    cls = TestClass(param1=0, param2="test")
    
    # Define known and unknown parameters
    kvs_known = {'param1': 1}
    kvs_unknown = {'extra_param': 'value'}
    kvs_mixed = {'param1': 1, 'extra_param': 'value'}
    
    # Test the function with mixed known and unknown parameters
    result_mixed = _separate_defined_undefined_kvs(cls, kvs_mixed)
    assert result_mixed == ({'param1': 1}, {'extra_param': 'value'})
    
    # Test the function with only known parameters
    result_known = _separate_defined_undefined_kvs(cls, kvs_known)
    assert result_known == ({'param1': 1}, {})
    
    # Test the function with only unknown parameters
    result_unknown = _separate_defined_undefined_kvs(cls, kvs_unknown)
    assert result_unknown == ({}, {'extra_param': 'value'})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_0.py:9:34: E1101: Module 'dataclasses_json.undefined' has no '_separate_defined_undefined_kvs' member (no-member)

"""