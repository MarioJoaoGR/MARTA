
import pytest
from ansible.module_utils.common.text.formatters import human_to_bytes

def test_valid_input_with_default_unit():
    result = human_to_bytes('10M')
    assert result == 10485760, f"Expected 10485760 bytes for '10M', but got {result}"

def test_valid_input_without_unit():
    result = human_to_bytes(10)
    assert result == 10, f"Expected 10 bytes for 10 without unit, but got {result}"

def test_invalid_input():
    with pytest.raises(ValueError):
        human_to_bytes('invalid')
