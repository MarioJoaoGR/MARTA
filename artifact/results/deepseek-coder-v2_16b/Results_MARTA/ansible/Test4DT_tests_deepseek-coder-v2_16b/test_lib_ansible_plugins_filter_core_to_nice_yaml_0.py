
import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import to_nice_yaml

def test_to_nice_yaml_with_valid_input():
    # Test with a valid dictionary input
    result = to_nice_yaml({'key': 'value'})
    assert isinstance(result, str), "Expected the output to be a string"
    assert len(result) > 0, "Expected the output to contain data"
