
import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.plugins.filter import mathstuff

# Assuming formatters is a placeholder for the actual module where human_to_bytes might be defined
formatters = mathstuff  # Placeholder to simulate the module context

def test_valid_input_basic():
    result = formatters.human_to_bytes('2G')
    assert result == 2 * (1024 ** 2)

def test_valid_input_specified_unit():
    result = formatters.human_to_bytes('512M', default_unit='M')
    assert result == 512 * (1024 ** 2)

def test_invalid_input():
    with pytest.raises(AnsibleFilterError):
        formatters.human_to_bytes('invalid input')
