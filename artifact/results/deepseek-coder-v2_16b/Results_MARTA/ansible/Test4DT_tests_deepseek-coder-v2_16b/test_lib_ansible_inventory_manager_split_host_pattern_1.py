
import pytest
from ansible.inventory.manager import split_host_pattern



def test_valid_string_input():
    pattern = 'a,b[1], c[2:3] , d'
    expected_output = ['a', 'b[1]', 'c[2:3]', 'd']
    assert split_host_pattern(pattern) == expected_output

def test_valid_list_input():
    pattern = ['a,b[1]', ' c[2:3] , d']
    expected_output = ['a', 'b[1]', 'c[2:3]', 'd']
    assert split_host_pattern(pattern) == expected_output
