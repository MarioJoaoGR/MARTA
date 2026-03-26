
import pytest
from collections import defaultdict
import typing
from dataclasses_json.utils import _is_mapping

# Helper function to mock _get_type_origin and _issubclass_safe for testing
def _get_type_origin(tp):
    return tp if not isinstance(tp, type) else tp.__origin__

def _issubclass_safe(cls, classinfo):
    return issubclass(cls, classinfo)

# Mocking the Mapping type from typing for testing purposes
Mapping = typing.Mapping

@pytest.mark.parametrize("type_, expected", [
    (dict, True),
    (defaultdict, True),
    ([], False),
    ({}, True),
    ("string", False),
    (int, False),
])
def test_is_mapping(type_, expected):
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_mapping_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0.py:25:38: E0001: Parsing failed: 'expected an indented block after function definition on line 25 (Test4DT_tests.test_dataclasses_json_utils__is_mapping_0, line 25)' (syntax-error)

"""