
import pytest
from ansible.module_utils.api import retry_argument_spec

def test_retry_argument_spec_default():
    result = retry_argument_spec()
    assert 'retries' in result, "Expected 'retries' key to be present"
    assert isinstance(result['retries'], int), "'retries' should be of type int"
    assert result['retry_pause'] == 1, "'retry_pause' should default to 1"

def test_retry_argument_spec_custom_spec():
    custom_spec = {'retry_pause': dict(type='float', default=2)}
    result = retry_argument_spec(custom_spec)
    assert 'retries' in result, "Expected 'retries' key to be present"
    assert isinstance(result['retries'], int), "'retries' should be of type int"
    assert isinstance(result['retry_pause'], float), "'retry_pause' should be of type float"
    assert result['retry_pause'] == 2, "Expected 'retry_pause' to be set to 2"

def test_retry_argument_spec_extend_spec():
    base_spec = retry_argument_spec()
    extended_spec = {'retries': dict(type='int', default=5)}
    final_spec = retry_argument_spec(extended_spec)
    assert 'retries' in final_spec, "Expected 'retries' key to be present"
    assert isinstance(final_spec['retries'], int), "'retries' should be of type int"
    assert final_spec['retries'] == 5, "Expected 'retries' to be set to 5"
    assert isinstance(final_spec['retry_pause'], float), "'retry_pause' should be of type float"
    assert final_spec['retry_pause'] == 1, "Expected 'retry_pause' to default to 1"
