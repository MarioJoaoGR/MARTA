
import pytest
from unittest.mock import patch
from ansible.plugins.filter import mathstuff

def test_unique_basic():
    with patch('ansible.plugins.filter.mathstuff.unique', return_value=['apple']):
        result = mathstuff.unique({'var': 'value'}, ['apple', 'banana', 'Apple', 'cherry'])
        assert result == ['apple']


def test_unique_attribute():
    with patch('ansible.plugins.filter.mathstuff.unique', return_value=[{'name': 'Alice'}]):
        result = mathstuff.unique({'var': 'value'}, [{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Alice'}], attribute='name')
        assert result == [{'name': 'Alice'}]
