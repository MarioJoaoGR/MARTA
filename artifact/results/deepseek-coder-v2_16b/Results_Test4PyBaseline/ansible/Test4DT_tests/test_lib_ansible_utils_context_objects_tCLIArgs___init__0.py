# Module: ansible.utils.context_objects
import pytest
from ansible.utils.context_objects import CLIArgs

# Test initialization with a basic dictionary
def test_basic_initialization():
    args = CLIArgs({'key1': 'value1', 'key2': [1, 2, {'nested_key': 'nested_value'}]})
    assert args['key1'] == 'value1'
    assert args['key2'][2]['nested_key'] == 'nested_value'

# Test initialization with a nested dictionary
def test_nested_initialization():
    complex_args = CLIArgs({'main_key': {'inner_key': 'inner_value', 'list_key': [1, 2, 3]}})
    assert complex_args['main_key']['inner_key'] == 'inner_value'
    assert complex_args['main_key']['list_key'][1] == 2

# Test initialization with an empty dictionary
def test_empty_initialization():
    empty_args = CLIArgs({})
    # Assuming 'empty_args' is expected to handle an empty dictionary gracefully
    assert isinstance(empty_args, CLIArgs)

# Test initialization with mixed data types
def test_mixed_data_types():
    mixed_args = CLIArgs({'string_key': 'a string', 'int_key': 123, 'list_key': [4, 5, {'nested_key': 'nested_value'}]})
    assert mixed_args['string_key'] == 'a string'
    assert mixed_args['int_key'] == 123
    assert mixed_args['list_key'][2]['nested_key'] == 'nested_value'
