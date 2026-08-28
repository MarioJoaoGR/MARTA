
import pytest
from lib.ansible.constants import _DeprecatedSequenceConstant

# Test case for valid input
def test_valid_input():
    deprecated_sequence = _DeprecatedSequenceConstant([1, 2, 3], "This sequence is deprecated.", "2.0")
    assert deprecated_sequence[1] == 2

# Test case for invalid input (should raise TypeError)
def test_invalid_input():
    with pytest.raises(TypeError):
        deprecated_sequence = _DeprecatedSequenceConstant([1, 2, 3], "This sequence is deprecated.", "2.0")
        deprecated_sequence[1] + "extra"
