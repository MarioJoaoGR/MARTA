
import pytest
from ansible.module_utils.api import rate_limit_argument_spec

def test_default_rate_limit_argument_spec():
    spec = rate_limit_argument_spec()
    assert isinstance(spec['rate'], dict) and spec['rate']['type'] == 'int'
    assert isinstance(spec['rate_limit'], dict) and spec['rate_limit']['type'] == 'int'

def test_customized_rate_limit_argument_spec():
    custom_spec = {'burst': dict(type='int')}
    spec = rate_limit_argument_spec(custom_spec)
    assert isinstance(spec['rate'], dict) and spec['rate']['type'] == 'int'
    assert isinstance(spec['rate_limit'], dict) and spec['rate_limit']['type'] == 'int'
    assert isinstance(spec['burst'], dict) and spec['burst']['type'] == 'int'
