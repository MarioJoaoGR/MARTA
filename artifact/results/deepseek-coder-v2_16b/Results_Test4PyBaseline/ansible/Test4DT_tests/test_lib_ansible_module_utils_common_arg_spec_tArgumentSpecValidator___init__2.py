
import pytest
from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
from ansible.errors import AnsibleError

# Test cases for the ArgumentSpecValidator class
def test_init():
    argument_spec = {
        'param1': {'type': str},
        'param2': {'type': int, 'required': True},
        'param3': {'nested': True}  # Nested argument spec for param3
    }
    
    validator = ArgumentSpecValidator(argument_spec,
                                       mutually_exclusive=['param1', 'param2'],
                                       required_together=[['param1', 'param2']],
                                       required_one_of=[[('param1', 'param2')]],
                                       required_if=[['param1', 1, ['param2']]],
                                       required_by={'param3': ['param1', 'param2']})
    
    assert validator._mutually_exclusive == ['param1', 'param2']
    assert validator._required_together == [['param1', 'param2']]
    assert validator._required_one_of == [[('param1', 'param2')]]
    assert validator._required_if == [['param1', 1, ['param2']]]
    assert validator._required_by == {'param3': ['param1', 'param2']}
    
    # Check that valid parameter names are set correctly
    expected_valid_parameter_names = {'param1', 'param2', 'param3'}
    for name in expected_valid_parameter_names:
        assert name in validator._valid_parameter_names

def test_init_with_aliases():
    argument_spec = {
        'param1': {'type': str},
        'param2': {'type': int, 'required': True, 'aliases': ['p2']},
        'param3': {'nested': True}  # Nested argument spec for param3
    }
    
    validator = ArgumentSpecValidator(argument_spec,
                                       mutually_exclusive=['param1', 'param2'],
                                       required_together=[['param1', 'param2']],
                                       required_one_of=[[('param1', 'param2')]],
                                       required_if=[['param1', 1, ['param2']]],
                                       required_by={'param3': ['param1', 'param2']})
    
    assert validator._mutually_exclusive == ['param1', 'param2']
    assert validator._required_together == [['param1', 'param2']]
    assert validator._required_one_of == [[('param1', 'param2')]]
    assert validator._required_if == [['param1', 1, ['param2']]]
    assert validator._required_by == {'param3': ['param1', 'param2']}
    
    # Check that valid parameter names with aliases are set correctly
    expected_valid_parameter_names = {'param1', 'param2 (p2)', 'param3'}
    for name in expected_valid_parameter_names:
        assert name in validator._valid_parameter_names

def test_init_with_nested():
    argument_spec = {
        'param1': {'type': str},
        'param2': {'type': int, 'required': True},
        'param3': {'nested': True}  # Nested argument spec for param3
    }
    
    validator = ArgumentSpecValidator(argument_spec,
                                       mutually_exclusive=['param1', 'param2'],
                                       required_together=[['param1', 'param2']],
                                       required_one_of=[[('param1', 'param2')]],
                                       required_if=[['param1', 1, ['param2']]],
                                       required_by={'param3': ['param1', 'param2']})
    
    assert validator._mutually_exclusive == ['param1', 'param2']
    assert validator._required_together == [['param1', 'param2']]
    assert validator._required_one_of == [[('param1', 'param2')]]
    assert validator._required_if == [['param1', 1, ['param2']]]