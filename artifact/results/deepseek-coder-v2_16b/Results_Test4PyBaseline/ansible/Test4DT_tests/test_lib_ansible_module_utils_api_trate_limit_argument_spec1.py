
import pytest
from ansible.module_utils.api import rate_limit_argument_spec

def test_rate_limit_argument_spec_basic():
    """Test the basic usage of rate_limit_argument_spec without additional specifications."""
    arg_spec = rate_limit_argument_spec()
    assert 'rate' in arg_spec
    assert 'rate_limit' in arg_spec