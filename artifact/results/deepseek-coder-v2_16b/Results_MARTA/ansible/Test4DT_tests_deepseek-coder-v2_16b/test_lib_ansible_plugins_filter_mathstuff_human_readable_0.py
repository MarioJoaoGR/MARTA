
import pytest
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError
from ansible.plugins.filter import mathstuff

# Assuming formatters is a module that contains bytes_to_human function
# from ansible.plugins.filter import mathstuff as formatters

def test_valid_input_default_unit():
    result = mathstuff.human_readable(1024)
    assert isinstance(result, str), "Expected a string"
    assert result == '1.0 KB', f"Unexpected result: {result}"

def test_valid_input_specified_unit():
    result = mathstuff.human_readable(1500, unit='MB')
    assert isinstance(result, str), "Expected a string"
    assert result == '1.5 MB', f"Unexpected result: {result}"

def test_invalid_input():
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        mathstuff.human_readable('not a number')
    assert str(excinfo.value) == "human_readable() failed on bad input: could not convert string to float: 'not a number'"
