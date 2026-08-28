
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.api import retry_never

def test_valid_inputs():
    with patch('ansible.module_utils.api.retry_never', return_value=False) as mock_retry_never:
        assert retry_never(Exception()) == False

def test_edge_cases():
    with patch('ansible.module_utils.api.retry_never', return_value=False) as mock_retry_never:
        assert retry_never(None) == False

def test_invalid_inputs():
    with patch('ansible.module_utils.api.retry_never', return_value=False) as mock_retry_never:
        assert retry_never("Invalid input") == False
