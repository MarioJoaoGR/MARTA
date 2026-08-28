
import pytest
from ansible.inventory.manager import split_host_pattern

# Test valid input scenario
def test_valid_input():
    pattern = 'a,b[1], c[2:3] , d'
    expected_output = ['a', 'b[1]', 'c[2:3]', 'd']
    assert split_host_pattern(pattern) == expected_output

# Test handling None input scenario
def test_none_input():
    pattern = None
    with pytest.raises(TypeError):
        split_host_pattern(pattern)

# Test handling invalid input type scenario
def test_invalid_input():
    pattern = 12345
    with pytest.raises(TypeError):
        split_host_pattern(pattern)
