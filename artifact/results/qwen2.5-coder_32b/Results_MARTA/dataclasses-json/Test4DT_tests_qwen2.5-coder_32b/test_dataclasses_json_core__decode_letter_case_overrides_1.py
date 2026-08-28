
import pytest
from dataclasses_json.core import _decode_letter_case_overrides






def test_decode_letter_case_overrides_with_no_overrides():
    """Test that no transformation occurs when no overrides are provided."""
    field_names = ['firstName', 'lastName']
    overrides = {}
    result = _decode_letter_case_overrides(field_names, overrides)
    assert result == {}
