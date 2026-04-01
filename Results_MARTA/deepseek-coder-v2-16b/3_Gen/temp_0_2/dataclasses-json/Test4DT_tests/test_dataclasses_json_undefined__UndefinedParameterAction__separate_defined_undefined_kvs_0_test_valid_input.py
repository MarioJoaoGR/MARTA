
from dataclasses import dataclass, fields
from typing import Dict, Tuple, List, Any
import pytest
from dataclasses_json.undefined import _UndefinedParameterAction  # Corrected import path

# Assuming _UndefinedParameterAction is defined in a module named 'dataclasses_json.undefined'

@pytest.fixture
def example_class():
    @dataclass
    class ExampleClass:
        field1: int
        field2: str
    return ExampleClass

def test_valid_input(example_class):
    kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(example_class, kvs)
    
    assert isinstance(known, dict), "Known parameters should be a dictionary"
    assert isinstance(unknown, dict), "Unknown parameters should be a dictionary"
    
    expected_known = {'field1': 1, 'field2': 'hello'}
    expected_unknown = {'extra_param': 'value'}
    
    assert known == expected_known, f"Expected known to be {expected_known}, but got {known}"
    assert unknown == expected_unknown, f"Expected unknown to be {expected_unknown}, but got {unknown}"
