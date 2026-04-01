
import pytest

def _as_list(value: str) -> list[str]:
    if isinstance(value, list):
        return [item.strip() for item in value]
    filtered = [item.strip() for item in value.replace("\n", ",").split(",") if item.strip()]
    return filtered

def test_valid_input_string():
    assert _as_list("apple, banana\ncherry") == ['apple', 'banana', 'cherry']
    assert _as_list([" apple ", " banana ", " cherry "]) == ['apple', 'banana', 'cherry']
    assert _as_list("apple\nbanana\ncherry") == ['apple', 'banana', 'cherry']
