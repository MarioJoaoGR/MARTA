
import pytest
from dataclasses import dataclass, fields
from typing import Optional
from dataclasses_json import core

# Assuming the following imports are needed for _decode_dataclass function
from dataclasses_json.core import (
    _isinstance_safe, _user_overrides_or_exts, _decode_letter_case_overrides,
    _handle_undefined_parameters_safe, get_type_hints, is_dataclass,
    _is_optional, _is_new_type, _is_supported_generic, _support_extended_types,
    MISSING
)

# Mock dataclass A with fields {'field1': int, 'field2': str}
@dataclass
class A:
    field1: int
    field2: str

def test_valid_inputs():
    # Define a valid JSON-compatible dictionary for the mock dataclass A
    valid_input = {'field1': 1, 'field2': 'test'}
    
    # Call the function with the mock dataclass and valid input
    result = core._decode_dataclass(A, valid_input, infer_missing=False)
    
    # Assert that the result is an instance of A and has the correct field values
    assert isinstance(result, A)
    assert result.field1 == 1
    assert result.field2 == 'test'
