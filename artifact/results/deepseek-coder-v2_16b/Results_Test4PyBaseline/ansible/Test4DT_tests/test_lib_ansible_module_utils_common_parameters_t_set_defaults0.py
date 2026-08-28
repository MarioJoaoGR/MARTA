
import pytest
from ansible.module_utils.common.parameters import _set_defaults

# Test cases for _set_defaults function
def test_set_defaults_with_no_log():
    argument_spec = {'param1': {'default': 1, 'no_log': False}, 'param2': {'default': None, 'no_log': True}}
    parameters = {}
    returned_values = _set_defaults(argument_spec, parameters)
    assert parameters == {'param1': 1, 'param2': None}
    assert list(returned_values) == [None]

def test_set_defaults_without_no_log():
    argument_spec = {'param1': {'default': 1, 'no_log': False}}
    parameters = {}
    returned_values = _set_defaults(argument_spec, parameters)
    assert parameters == {'param1': 1}
    assert list(returned_values) == []

def test_set_defaults_with_logging_masked():
    argument_spec = {'param2': {'default': None, 'no_log': True}}
    parameters = {}
    returned_values = _set_defaults(argument_spec, parameters)
    assert parameters == {'param2': None}
    assert list(returned_values) == [None]

def test_not_setting_defaults():
    argument_spec = {'param1': {'default': 1, 'no_log': False}}
    parameters = {'param1': None}  # User provided a value for param1
    returned_values = _set_defaults(argument_spec, parameters)
    assert parameters == {'param1': None}  # Unchanged since user provided a value
    assert list(returned_values) == []

def test_not_setting_defaults_with_no_log():
    argument_spec = {'param2': {'default': None, 'no_log': True}}
    parameters = {'param2': 1}  # User provided a value for param2
    returned_values = _set_defaults(argument_spec, parameters)
    assert parameters == {'param2': None}  # Default set to None since user did not provide one
    assert list(returned_values) == [None]

def test_not_setting_defaults_when_false():
    argument_spec = {'param1': {'default': 1, 'no_log': False}}
    parameters = {}
    returned_values = _set_defaults(argument_spec, parameters, set_default=False)
    assert parameters == {}
    assert list(returned_values) == []
