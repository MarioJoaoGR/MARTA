
import re
import pytest
from ansible.module_utils.common.text.formatters import human_to_bytes, SIZE_RANGES

# Test cases for converting numbers with specified units to bytes or bits
def test_human_to_bytes_with_unit():
    assert human_to_bytes('10MB') == 10485760
    assert human_to_bytes(10, 'M') == 10485760

# Test cases for invalid inputs that should raise ValueError
def test_human_to_bytes_invalid_inputs():
    with pytest.raises(ValueError) as excinfo:
        human_to_bytes('10Mb')  # 'b' is for bits, not bytes