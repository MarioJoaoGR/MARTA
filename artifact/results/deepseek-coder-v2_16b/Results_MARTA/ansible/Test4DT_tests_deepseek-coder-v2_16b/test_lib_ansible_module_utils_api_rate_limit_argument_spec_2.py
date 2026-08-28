
import pytest
from ansible.module_utils.api import rate_limit_argument_spec

def test_valid_input():
    valid_input = {'rate': 10, 'rate_limit': 20}
    result = rate_limit_argument_spec(valid_input)
    assert isinstance(result, dict), "Expected a dictionary"
    assert set(result.keys()) == {'rate', 'rate_limit'}, "Expected keys are 'rate' and 'rate_limit'"
    assert all(isinstance(value, int) for value in result.values()), "All values should be integers"
