
import pytest
from ansible.utils.color import colorize

# Test valid input scenario
def test_valid_input():
    result = colorize("Result", 42, "green")
    assert isinstance(result, str), "Expected a string output"
    assert result == "Result=42", f"Expected 'Result=42', but got {result}"

# Test edge case scenario with None as lead
def test_edge_case():
    result = colorize(None, 0, "default")
    assert isinstance(result, str), "Expected a string output"
    assert result == "None=0", f"Expected 'None=0', but got {result}"

# Test invalid input scenario raising TypeError
def test_invalid_input():
    with pytest.raises(TypeError):
        colorize()
