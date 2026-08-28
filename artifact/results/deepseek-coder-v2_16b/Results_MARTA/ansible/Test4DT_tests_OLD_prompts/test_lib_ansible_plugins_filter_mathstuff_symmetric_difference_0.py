
import pytest
from ansible.plugins.filter import mathstuff
from unittest.mock import patch

def test_symmetric_difference_with_hashable():
    with patch('ansible.plugins.filter.mathstuff.intersect', return_value=set()):
        with patch('ansible.plugins.filter.mathstuff.union', return_value=set()):
            result = mathstuff.symmetric_difference({'var': 'value'}, [1, 2, 3], [3, 4, 5])
    assert result == []

def test_symmetric_difference_with_non_hashable():
    with patch('ansible.plugins.filter.mathstuff.intersect', return_value=[3]):
        with patch('ansible.plugins.filter.mathstuff.union', return_value=[1, 2, 3, 4, 5]):
            result = mathstuff.symmetric_difference({'var': 'value'}, [1, 2, 3], [3, 4, 5])
    assert result == [1, 2, 4, 5]
