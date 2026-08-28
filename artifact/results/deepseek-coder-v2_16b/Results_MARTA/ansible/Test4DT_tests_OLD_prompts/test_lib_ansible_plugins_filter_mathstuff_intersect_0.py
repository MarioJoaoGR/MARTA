
import pytest
from ansible.plugins.filter.mathstuff import intersect, unique
from unittest.mock import patch



def test_valid_input():
    environment = {'var': 'value'}
    
    # Test with valid inputs
    a = [1, 2, 3]
    b = [2, 3, 4]
    with patch('ansible.plugins.filter.mathstuff.unique', return_value=[2, 3]):
        result = intersect(environment, a, b)
        assert result == [2, 3]