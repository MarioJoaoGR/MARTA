
import pytest
from ansible.template.native_helpers import ansible_native_concat

# Test scenarios for ansible_native_concat function

def test_valid_input_single_node():
    nodes = [1, 2, 3]
    result = ansible_native_concat(nodes)
    assert result == 123

def test_valid_input_multiple_nodes():
    nodes = ['a', 'b', 'c']
    result = ansible_native_concat(nodes)
    assert result == 'abc'

def test_invalid_input_empty_list():
    nodes = []
    result = ansible_native_concat(nodes)
    assert result is None
