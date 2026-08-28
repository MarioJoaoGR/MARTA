
import pytest
from ansible.module_utils.api import retry_argument_spec

def test_retry_argument_spec_default():
    result = retry_argument_spec()
    assert 'retries' in result, "Expected 'retries' key to be present"