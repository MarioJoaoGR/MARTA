
import pytest
from ansible.plugins.action.copy import _create_remote_copy_args

def test__create_remote_copy_args_basic():
    original_dict = {'action': 'copy', 'source': '/local/path', 'destination': '/remote/path'}
    filtered_dict = _create_remote_copy_args(original_dict)
    expected_output = {'action': 'copy', 'source': '/local/path', 'destination': '/remote/path'}
    assert filtered_dict == expected_output, f"Expected {expected_output}, but got {filtered_dict}"


def test__create_remote_copy_args_empty():
    original_dict = {}
    filtered_dict = _create_remote_copy_args(original_dict)
    expected_output = {}
    assert filtered_dict == expected_output, f"Expected {expected_output}, but got {filtered_dict}"
