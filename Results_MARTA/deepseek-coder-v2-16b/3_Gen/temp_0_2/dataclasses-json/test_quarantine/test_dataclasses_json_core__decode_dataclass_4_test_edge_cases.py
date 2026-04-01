
import pytest
from dataclasses import dataclass, fields, MISSING
from typing import Optional, get_type_hints
import warnings
from dataclasses_json.core import (
    _isinstance_safe, _user_overrides_or_exts, _decode_letter_case_overrides,
    _handle_undefined_parameters_safe, is_dataclass, get_type_hints, fields
)
from dataclasses_json.core import (
    _is_optional, _is_new_type, _is_supported_generic, _support_extended_types,
    _decode_generic, _decode_dataclass
)

@pytest.mark.parametrize("cls, kvs, infer_missing", [
    (None, {}, True),  # Test with None class
    ({}, {}, False),   # Test with empty dictionary for kvs
    (int, None, True), # Test with int as cls and None for kvs
])
def test_edge_cases(cls, kvs, infer_missing):
    with pytest.raises(TypeError):
        _decode_dataclass(cls, kvs, infer_missing)
