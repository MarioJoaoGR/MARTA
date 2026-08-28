
import pytest
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError
from unittest.mock import patch
from ansible.plugins.filter.mathstuff import human_readable

def test_valid_input_default_unit():
    with patch('ansible.plugins.filter.mathstuff.formatters.bytes_to_human') as mock_formatter:
        result = human_readable(1024)
        assert result is not None, "Expected a non-None value"
        mock_formatter.assert_called_once_with(1024, False, None)

def test_valid_input_specified_unit():
    with patch('ansible.plugins.filter.mathstuff.formatters.bytes_to_human') as mock_formatter:
        result = human_readable(1024, unit='KB')
        assert result is not None, "Expected a non-None value"
        mock_formatter.assert_called_once_with(1024, False, 'KB')

def test_invalid_input():
    with pytest.raises(AnsibleFilterTypeError):
        human_readable('not a number')
