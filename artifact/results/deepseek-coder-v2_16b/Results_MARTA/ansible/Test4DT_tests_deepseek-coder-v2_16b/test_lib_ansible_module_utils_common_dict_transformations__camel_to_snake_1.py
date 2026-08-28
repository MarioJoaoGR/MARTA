
import pytest
import re
from ansible.module_utils.common.dict_transformations import _camel_to_snake

# Test Scenario 1: Test standard input with valid camelCase string
def test_valid_input_standard():
    result = _camel_to_snake("CamelCaseName", False)
    assert result == "camel_case_name"

# Test Scenario 2: Test reversible flag set to True for handling pluralized abbreviations
def test_reversible_true():
    result = _camel_to_snake("TargetGroupARNs", True)
    assert result == "target_group_ar_ns"

# Test Scenario 3: Test invalid input, expecting ValueError or TypeError
def test_invalid_input():
    with pytest.raises(ValueError):
        _camel_to_snake("InvalidInput")
