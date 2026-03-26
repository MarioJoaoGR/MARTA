
import pytest
from dataclasses import fields, make_dataclass
from typing import Dict, Tuple, List
from _UndefinedParameterAction import _separate_defined_undefined_kvs

# Define a test class for the purpose of testing
class ExampleClass:
    field1: int
    field2: str

def test_valid_input():
    # Create a dataclass from the fields of ExampleClass
    cls = make_dataclass('TestClass', [(field.name, field.type) for field in fields(ExampleClass)])
    
    # Define valid key-value pairs
    kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
    
    # Call the function under test
    known, unknown = _separate_defined_undefined_kvs(cls, kvs)
    
    # Define expected outputs
    expected_known = {'field1': 1, 'field2': 'hello'}
    expected_unknown = {'extra_param': 'value'}
    
    # Assert that the known and unknown dictionaries match the expected results
    assert known == expected_known
    assert unknown == expected_unknown

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction__separate_defined_undefined_kvs_0_test_valid_input.py:5:0: E0401: Unable to import '_UndefinedParameterAction' (import-error)


"""