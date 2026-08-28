
import pytest
from unittest.mock import patch
from ansible.plugins.action.copy import _create_remote_copy_args


def test_create_remote_copy_args_basic():
    input_dict = {'action': 'copy', 'source': '/local/path', 'destination': '/remote/path', 'content': 'file_content', 'decrypt': True}
    expected_output = {'action': 'copy', 'source': '/local/path', 'destination': '/remote/path'}
    with patch('ansible.plugins.action.copy._create_remote_copy_args', return_value=expected_output):
        result = _create_remote_copy_args(input_dict)
        assert result == expected_output

def test_create_remote_copy_args_no_extra_keys():
    input_dict = {'action': 'copy', 'source': '/local/path', 'destination': '/remote/path'}
    expected_output = {'action': 'copy', 'source': '/local/path', 'destination': '/remote/path'}
    with patch('ansible.plugins.action.copy._create_remote_copy_args', return_value=expected_output):
        result = _create_remote_copy_args(input_dict)
        assert result == expected_output


def test_create_remote_copy_args_empty_dict():
    input_dict = {}
    expected_output = {}
    with patch('ansible.plugins.action.copy._create_remote_copy_args', return_value=expected_output):
        result = _create_remote_copy_args(input_dict)
        assert result == expected_output