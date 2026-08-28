
import pytest
from unittest.mock import patch
from lib.ansible.plugins.action import ActionModule

# Test for valid file extension
def test_valid_file_extension():
    am = ActionModule()
    with patch('lib.ansible.plugins.action.ActionModule._is_valid_file_ext') as mock_is_valid:
        mock_is_valid.return_value = True
        assert am._is_valid_file_ext('example.yaml') == True
        assert am._is_valid_file_ext('example.yml') == True
        assert am._is_valid_file_ext('example.json') == True
        assert am._is_valid_file_ext('example.txt') == False

# Test for invalid file extension
def test_invalid_file_extension():
    am = ActionModule()
    with patch('lib.ansible.plugins.action.ActionModule._is_valid_file_ext') as mock_is_valid:
        mock_is_valid.return_value = False
        assert am._is_valid_file_ext('example.txt') == False
        assert am._is_valid_file_ext('example.yaml') == False
        assert am._is_valid_file_ext('example.yml') == False
        assert am._is_valid_file_ext('example.json') == False

# Test handling of None input
def test_none_input():
    am = ActionModule()
    with pytest.raises(TypeError):
        assert am._is_valid_file_ext(None)
