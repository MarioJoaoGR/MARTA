
import os
import json
from unittest.mock import patch, MagicMock
import pytest
from cookiecutter.replay import load

# Helper function to mock get_file_name
@patch('cookiecutter.replay.get_file_name', return_value='mocked_file_path')
def test_load_valid_json(mock_get_file_name):
    with patch('builtins.open', create=True) as mock_open:
        mock_data = {'cookiecutter': {}}
        mock_open.return_value.__enter__.return_value.read.return_value = json.dumps(mock_data)
        
        context = load('replay_dir', 'template_name')
        assert context == mock_data
        mock_get_file_name.assert_called_once_with('replay_dir', 'template_name')

# Test for invalid template name type
def test_load_invalid_type():
    with pytest.raises(TypeError):
        load('replay_dir', 123)

# Test for missing cookiecutter key in context
@patch('builtins.open', create=True) as mock_open:
    def test_load_missing_cookiecutter_key():
        mock_data = {'not_cookiecutter': {}}
        mock_open.return_value.__enter__.return_value.read.return_value = json.dumps(mock_data)
        
        with pytest.raises(ValueError):
            load('replay_dir', 'template_name')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax (line 25, col 38)
@patch('builtins.open', create=True) as mock_open:
"""