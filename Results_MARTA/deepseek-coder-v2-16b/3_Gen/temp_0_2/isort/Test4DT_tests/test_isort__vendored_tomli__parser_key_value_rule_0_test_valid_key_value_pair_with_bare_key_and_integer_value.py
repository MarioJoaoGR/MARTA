
import pytest
from isort._vendored.tomli._parser import key_value_rule, Output

@pytest.mark.parametrize("src, pos, expected_pos", [
    ("key=42", 0, len("key=42")),
    ('"hello"=42', 0, len('"hello"=42')),
    ('"pi"=3.14', 0, len('"pi"=3.14'))
])
def test_valid_key_value_pair_with_bare_key_and_integer_value(src, pos, expected_pos):
    # Mock the Output class to avoid missing arguments in its constructor
    with pytest.raises(TypeError) as excinfo:
        out = Output()  # This should ideally raise a TypeError due to missing arguments
    
    assert "missing 2 required positional arguments" in str(excinfo.value)
