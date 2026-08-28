
import pytest
from ansible.plugins.filter import mathstuff
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError

def test_valid_input_happy_path():
    # Test valid input with human-readable byte strings
    assert mathstuff.human_to_bytes('2G') == 2147483648
    assert mathstuff.human_to_bytes('512M', default_unit='M') == 512 * 1024 ** 2

