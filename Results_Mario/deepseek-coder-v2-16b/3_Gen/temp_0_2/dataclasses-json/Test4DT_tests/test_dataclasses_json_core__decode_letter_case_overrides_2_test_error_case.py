
import pytest
from dataclasses_json.core import _decode_letter_case_overrides

def test_error_case():
    field_names = None
    overrides = None
    
    # Test when both field_names and overrides are None
    with pytest.raises(TypeError):
        _decode_letter_case_overrides(field_names, overrides)
