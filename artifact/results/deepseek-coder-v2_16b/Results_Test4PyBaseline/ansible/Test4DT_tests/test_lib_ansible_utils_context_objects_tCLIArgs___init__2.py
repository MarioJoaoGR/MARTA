
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
    mixed_args = CLIArgs({'string_key': 'a string', 'int_key': 42, 'nested_dict': {'nested_key': True}})
    assert mixed_args['string_key'] == 'a string'
    assert mixed_args['int_key'] == 42
    assert mixed_args['nested_dict']['nested_key'] is True

# Test initialization with a dictionary containing mutable types
def test_mutable_types_in_dictionary():
    mutable_dict = CLIArgs({'mutable': {'set': set([1, 2]), 'list': [1, 2]}, 'string': 'a string'})
    assert isinstance(mutable_dict['mutable']['set'], frozenset)
    assert isinstance(mutable_dict['mutable']['list'], tuple)
    assert mutable_dict['string'] == 'a string'

# Test initialization with a list containing mutable types
def test_mutable_types_in_list():
    mutable_list = CLIArgs({'list': [1, 2, {'set': set([3, 4])}]})
    assert isinstance(mutable_list['list'][2]['set'], frozenset)

# Test initialization with a dictionary containing nested mutable types
def test_nested_mutable_types():
    nested_mutable = CLIArgs({'outer': {'inner': {'set': set([5, 6]), 'list': [7, 8]}}})
    assert isinstance(nested_mutable['outer']['inner']['set'], frozenset)
    assert isinstance(nested_mutable['outer']['inner']['list'], tuple)

# Test initialization with a dictionary containing both mutable and immutable types
def test_mixed_types():
    mixed_types = CLIArgs({'immutable': 'a string', 'mutable': {'set': set([9, 10]), 'dict': {}}})
    assert isinstance(mixed_types['immutable'], str)
    assert isinstance(mixed_types['mutable']['set'], frozenset)