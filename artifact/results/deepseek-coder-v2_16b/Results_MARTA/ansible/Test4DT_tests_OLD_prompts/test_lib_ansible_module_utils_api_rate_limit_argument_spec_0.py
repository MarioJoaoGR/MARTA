
import pytest
from ansible.module_utils.api import rate_limit_argument_spec

def test_rate_limit_argument_spec_default():
    default_arg_spec = rate_limit_argument_spec()
    assert isinstance(default_arg_spec['rate'], dict) and default_arg_spec['rate']['type'] == 'int'
    assert isinstance(default_arg_spec['rate_limit'], dict) and default_arg_spec['rate_limit']['type'] == 'int'

def test_rate_limit_argument_spec_with_custom():
    custom_spec = {'burst': dict(type='int')}
    customized_arg_spec = rate_limit_argument_spec(custom_spec)
    assert isinstance(customized_arg_spec['rate'], dict) and customized_arg_spec['rate']['type'] == 'int'
    assert isinstance(customized_arg_spec['rate_limit'], dict) and customized_arg_spec['rate_limit']['type'] == 'int'
    assert isinstance(customized_arg_spec['burst'], dict) and customized_arg_spec['burst']['type'] == 'int'

def test_rate_limit_argument_spec_invalid_input():
    with pytest.raises(ValueError):
        rate_limit_argument_spec('not_a_dict')
