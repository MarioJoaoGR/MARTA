
import pytest
from string_utils.generation import generate

def roman_encode(n):
    """Convert an integer to a Roman numeral."""
    romans = ["I", "V", "X", "L", "C", "D", "M"]
    values = [1, 5, 10, 50, 100, 500, 1000]
    result = ""
    for i in range(len(values)):
        while n >= values[i]:
            result += romans[i]
            n -= values[i]
    return result

@pytest.mark.parametrize("start, stop, step", [
    (1, 5, 0),       # Step is zero, should raise ValueError
    (-1, 5, 1),     # Negative start, should raise ValueError
    (1, -5, 1),     # Negative stop, should raise ValueError
    (1, 5, -1),     # Negative step, should raise ValueError
    ('a', 5, 1),     # Non-integer start, should raise TypeError
    (1, 'b', 1),     # Non-integer stop, should raise TypeError
    (1, 5, 'c'),     # Non-integer step, should raise TypeError
])
def test_invalid_input(start, stop, step):
    with pytest.raises(ValueError) as excinfo:
        list(generate(start=start, stop=stop, step=step, roman_encode=roman_encode))
    assert str(excinfo.value) == "Step must be a positive integer."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_generation_generate_0_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_generation_generate_0_test_invalid_input.py:3:0: E0611: No name 'generate' in module 'string_utils.generation' (no-name-in-module)


"""