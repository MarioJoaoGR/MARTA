
import pytest
from ansible.inventory.manager import split_host_pattern



def test_split_host_pattern_with_string():
    pattern = 'a,b[1], c[2:3] , d'
    expected = ['a', 'b[1]', 'c[2:3]', 'd']
    assert split_host_pattern(pattern) == expected

def test_split_host_pattern_with_list():
    pattern = ['a,b[1]', ' c[2:3] , d']
    expected = ['a', 'b[1]', 'c[2:3]', 'd']
    assert split_host_pattern(pattern) == expected