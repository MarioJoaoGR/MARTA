
import pytest
from ansible.module_utils.api import rate_limit_argument_spec

def test_rate_limit_argument_spec_default():
    arg_spec = rate_limit_argument_spec()
    assert isinstance(arg_spec['rate'], dict) and arg_spec['rate']['type'] == 'int'
    assert isinstance(arg_spec['rate_limit'], dict) and arg_spec['rate_limit']['type'] == 'int'

def test_rate_limit_argument_spec_with_custom_spec():
    custom_spec = {'burst': dict(type='int')}
    arg_spec = rate_limit_argument_spec(custom_spec)
    assert isinstance(arg_spec['rate'], dict) and arg_spec['rate']['type'] == 'int'
    assert isinstance(arg_spec['rate_limit'], dict) and arg_spec['rate_limit']['type'] == 'int'
    assert isinstance(arg_spec['burst'], dict) and arg_spec['burst']['type'] == 'int'
