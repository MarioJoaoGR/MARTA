
import pytest
from ansible.module_utils.common.text.formatters import human_to_bytes

# Test cases for converting numbers with specified units to bytes or bits
def test_human_to_bytes_with_unit():
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes('1Mb', isbits=True) == 1048576

# Test cases for invalid inputs that should raise exceptions
def test_human_to_bytes_invalid_inputs():
    with pytest.raises(ValueError) as excinfo:
        human_to_bytes('invalid input')