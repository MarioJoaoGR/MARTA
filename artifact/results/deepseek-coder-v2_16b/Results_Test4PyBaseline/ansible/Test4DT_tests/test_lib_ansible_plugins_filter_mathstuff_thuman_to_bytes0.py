# Module: ansible.plugins.filter.mathstuff
import pytest
from ansible.plugins.filter import mathstuff

# Test cases for human_to_bytes function
def test_human_to_bytes_default():
    assert mathstuff.human_to_bytes("10K") == 10240

def test_human_to_bytes_with_default_unit():
    assert mathstuff.human_to_bytes("5M", default_unit="B") == 5242880

def test_human_to_bytes_as_bits():
    assert mathstuff.human_to_bytes("3G", isbits=True) == 31457280

# Edge cases to consider:
# - Invalid input strings should raise AnsibleFilterError
# - Non-string inputs should raise TypeError
def test_human_to_bytes_invalid_input():
    with pytest.raises(mathstuff.AnsibleFilterError):
        mathstuff.human_to_bytes("invalid input")

def test_human_to_bytes_non_string_input():
    with pytest.raises(mathstuff.AnsibleFilterTypeError):
        mathstuff.human_to_bytes(12345)
