
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