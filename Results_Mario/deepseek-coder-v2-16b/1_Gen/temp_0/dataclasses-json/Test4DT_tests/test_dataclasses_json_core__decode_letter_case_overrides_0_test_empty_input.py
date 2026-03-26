
import pytest
from dataclasses_json.core import _decode_letter_case_overrides

def test_empty_input():
    field_names = []
    overrides = {}
    
    result = _decode_letter_case_overrides(field_names, overrides)
    
    assert isinstance(result, dict), "The result should be a dictionary"
    assert len(result) == 0, "The dictionary should be empty for no field names and no overrides"
