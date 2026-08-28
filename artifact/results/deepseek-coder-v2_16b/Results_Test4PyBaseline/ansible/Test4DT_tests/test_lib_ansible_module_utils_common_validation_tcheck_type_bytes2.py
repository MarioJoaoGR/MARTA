
import pytest
from ansible.module_utils.common.validation import check_type_bytes

# Test cases for check_type_bytes function
def test_check_type_bytes_valid():
    assert check_type_bytes('1024B') == 1024
    assert check_type_bytes('5KB') == 5 * 1024
    assert check_type_bytes('1MB') == 1 * 1024 * 1024

# Test cases for invalid inputs that should raise TypeError
def test_check_type_bytes_invalid():
    with pytest.raises(TypeError) as excinfo:
        check_type_bytes('invalid input')