
import pytest
from unittest.mock import patch, MagicMock
from random import SystemRandom, Random
from ansible.plugins.filter.core import rand

def test_valid_case_1():
    with patch('ansible.plugins.filter.core.SystemRandom') as mock_random:
        mock_instance = mock_random.return_value
        mock_instance.randrange.return_value = 4
        result = rand(None, 10, start=0, step=2)
        assert result == 4
        mock_instance.randrange.assert_called_once_with(0, 10, 2)

def test_valid_case_2():
    with patch('ansible.plugins.filter.core.SystemRandom') as mock_random:
        mock_instance = mock_random.return_value
        mock_instance.choice.return_value = 3
        result = rand(None, [1, 2, 3, 4, 5])
        assert result == 3
        mock_instance.choice.assert_called_once_with([1, 2, 3, 4, 5])

def test_error_case_1():
    with pytest.raises(Exception) as e:
        rand(None, 'not an integer', start=0, step=2)
    assert str(e.value) == 'start and step can only be used with integer values'
