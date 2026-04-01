
import pytest
from dataclasses_json.core import _decode_letter_case_overrides

def test_empty_input():
    field_names = []
    overrides = {}
    result = _decode_letter_case_overrides(field_names, overrides)
    assert result == {}, "Expected an empty dictionary for both empty inputs"
