
import pytest
from ansible.plugins.filter.core import strftime
from ansible.errors import AnsibleFilterError
import time
from unittest.mock import patch, MagicMock

def test_valid_input_happy_path():
    with patch('time.localtime') as mock_localtime:
        mock_localtime.return_value = time.struct_time((2023, 4, 1, 12, 34, 56, 6, 90, -1))
        assert strftime('%Y-%m-%d %H:%M:%S', 1680579296.0) == '2023-04-01 12:34:56'

def test_edge_case_none():
    with patch('time.localtime') as mock_localtime:
        mock_localtime.return_value = time.struct_time((2023, 4, 1, 12, 34, 56, 6, 90, -1))
        assert strftime('%Y-%m-%d %H:%M:%S') == '2023-04-01 12:34:56'

def test_invalid_input_error_handling():
    with pytest.raises(AnsibleFilterError):
        strftime('%Y-%m-%d %H:%M:%S', 'not_a_number')
