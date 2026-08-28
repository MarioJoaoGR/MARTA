
import pytest
from ansible.utils.context_objects import CLIArgs

# Test creating an instance with a simple dictionary
def test_simple_dictionary():
    args = CLIArgs({'key1': 'value1', 'key2': [1, 2, {'nested_key': 'nested_value'}]})
    assert args['key1'] == 'value1'
    assert args['key2'][2]['nested_key'] == 'nested_value'

# Test creating an instance with a more complex dictionary
def test_complex_dictionary():
    args = CLIArgs({'complex': {'nested': 'value', 'list': [1, 2, 3], 'dict': {'inner': 'inner_value'}}})
    assert args['complex']['nested'] == 'value'
    assert args['complex']['list'][0] == 1
    assert args['complex']['dict']['inner'] == 'inner_value'

# Test using the from_options class method to create an instance
def test_from_options():
    options = {'key1': 'value1', 'key2': [1, 2, {'nested_key': 'nested_value'}]}
    args = CLIArgs.from_options(options)
    assert args['key1'] == 'value1'
    assert args['key2'][2]['nested_key'] == 'nested_value'

# Test handling of basic data types (should not modify strings or basic data types)
def test_basic_data_types():
    args = CLIArgs({'key': 'value'})
    assert isinstance(args['key'], str)  # Ensure it remains a string

# Edge case: Passing an empty dictionary
def test_empty_dictionary():
    args = CLIArgs({})
    with pytest.raises(KeyError):
        print(args['non_existent_key'])  # Should raise KeyError as the key does not exist
