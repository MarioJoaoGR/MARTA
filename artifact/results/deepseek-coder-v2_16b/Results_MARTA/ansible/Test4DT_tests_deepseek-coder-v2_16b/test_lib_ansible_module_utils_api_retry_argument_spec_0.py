
import pytest
from ansible.module_utils.api import retry_argument_spec

def test_retry_argument_spec_default():
    """Test default values in retry_argument_spec"""
    spec = retry_argument_spec()
    assert 'retries' in spec
    assert spec['retries']['type'] == 'int'
    assert 'retry_pause' in spec
    assert spec['retry_pause']['type'] == 'float'
    assert spec['retry_pause']['default'] == 1

def test_retry_argument_spec_custom():
    """Test custom specification in retry_argument_spec"""
    custom_spec = {'timeout': dict(type='float', default=30)}
    spec = retry_argument_spec(custom_spec)
    assert 'retries' in spec
    assert spec['retries']['type'] == 'int'
    assert 'retry_pause' in spec
    assert spec['retry_pause']['type'] == 'float'
    assert spec['retry_pause']['default'] == 1
    assert 'timeout' in spec
    assert spec['timeout']['type'] == 'float'
    assert spec['timeout']['default'] == 30

def test_retry_argument_spec_update():
    """Test updating existing argument specification"""
    existing_spec = {'max_attempts': dict(type='int', default=5)}
    updated_spec = retry_argument_spec(existing_spec)
    assert 'retries' in updated_spec
    assert updated_spec['retries']['type'] == 'int'
    assert 'retry_pause' in updated_spec
    assert updated_spec['retry_pause']['type'] == 'float'
    assert updated_spec['retry_pause']['default'] == 1
    assert 'max_attempts' in updated_spec
    assert updated_spec['max_attempts']['type'] == 'int'
    assert updated_spec['max_attempts']['default'] == 5
