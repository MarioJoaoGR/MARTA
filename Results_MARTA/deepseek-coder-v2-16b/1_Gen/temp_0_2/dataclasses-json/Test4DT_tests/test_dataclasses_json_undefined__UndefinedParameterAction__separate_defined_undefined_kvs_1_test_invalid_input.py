
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Tuple, List, Any
from dataclasses_json.undefined import _UndefinedParameterAction

@pytest.fixture(name="class_with_fields")
def fixture_class_with_fields():
    @dataclass
    class ExampleClass:
        param1: int
        param2: str
    
    return ExampleClass

def test_invalid_input(class_with_fields):
    # Arrange
    kvs = {'param1': 1, 'extra_param': 'unknown'}
    expected_known = {'param1': 1}
    expected_unknown = {'extra_param': 'unknown'}
    
    # Act
    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(class_with_fields, kvs)
    
    # Assert
    assert known == expected_known
    assert unknown == expected_unknown
