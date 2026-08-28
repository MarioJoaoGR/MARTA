
import pytest
from ansible.utils.context_objects import CLIArgs, _make_immutable

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

# Test initialization with a dictionary containing basic data types
def test_basic_data_types():
    basic_types = CLIArgs({'str': 'hello', 'int': 1, 'float': 3.14, 'bool': False})
    assert basic_types['str'] == 'hello'
    assert basic_types['int'] == 1
    assert basic_types['float'] == 3.14
    assert basic_types['bool'] is False

# Test initialization with a dictionary containing nested lists and sets
def test_nested_lists_and_sets():
    nested_structure = CLIArgs({'list': [1, 2, {'set': {1, 2, 3}}], 'set': {4, 5, frozenset([6, 7, 8])}})
    assert isinstance(nested_structure['list'][2]['set'], frozenset)
    assert nested_structure['set'] == {4, 5, frozenset([6, 7, 8])}

# Test initialization with a dictionary containing deeply nested structures
def test_deeply_nested():
    deeply_nested = CLIArgs({'level1': {'level2': {'level3': {'key': 'value'}}}})
    assert deeply_nested['level1']['level2']['level3']['key'] == 'value'

# Test initialization with a dictionary containing mixed keys (strings, numbers)
def test_mixed_keys():
    mixed_keys = CLIArgs({'str_key': 'string', 1: [1, 2, {'set': {1}}], 'nested': {'another_str': 'another string'}})
    assert mixed_keys['str_key'] == 'string'
    assert mixed_keys[1][1] == 2
    assert isinstance(mixed_keys['nested']['another_str'], str)

# Test initialization with an empty dictionary to ensure it handles it gracefully
def test_empty_dict():
    empty_args = CLIArgs({})
    assert len(empty_args) == 0
