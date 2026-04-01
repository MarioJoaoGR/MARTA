
import pytest

def _as_list(value: str) -> list[str]:
    if isinstance(value, list):
        return [item.strip() for item in value]
    filtered = [item.strip() for item in value.replace("\n", ",").split(",") if item.strip()]
    return filtered

def test_valid_input_newline_separated():
    value = 'apple\nbanana\norange'
    expected_output = ['apple', 'banana', 'orange']
    assert _as_list(value) == expected_output
