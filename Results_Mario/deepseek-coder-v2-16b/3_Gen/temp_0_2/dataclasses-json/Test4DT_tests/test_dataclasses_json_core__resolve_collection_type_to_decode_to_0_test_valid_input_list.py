
import pytest
from dataclasses import dataclass
from typing import List, Dict
import collections.abc as abc
from dataclasses_json.core import _resolve_collection_type_to_decode_to

@pytest.mark.parametrize("input_type, expected_output", [
    (List[int], list),
    (Dict[str, int], dict),
    (list, list),  # Ensure it returns the original type if already a list
    (dict, dict)   # Ensure it returns the original type if already a dictionary
])
def test_resolve_collection_type_to_decode_to(input_type, expected_output):
    resolved_type = _resolve_collection_type_to_decode_to(input_type)
    assert isinstance(resolved_type, type) and issubclass(resolved_type, abc.Collection), \
        f"Expected {expected_output} but got {resolved_type}"
    assert resolved_type == expected_output, f"Expected {expected_output} but got {resolved_type}"
