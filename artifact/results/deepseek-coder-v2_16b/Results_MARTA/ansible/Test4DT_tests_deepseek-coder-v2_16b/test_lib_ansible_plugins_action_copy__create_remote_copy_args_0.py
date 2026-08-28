
import pytest
from ansible.plugins.action.copy import _create_remote_copy_args



def test_no_extra_keys():
    original_dict = {'action': 'copy', 'source': '/local/path', 'destination': '/remote/path'}
    expected_dict = {'action': 'copy', 'source': '/local/path', 'destination': '/remote/path'}
    filtered_dict = _create_remote_copy_args(original_dict)
    assert filtered_dict == expected_dict

def test_empty_input():
    original_dict = {}
    expected_dict = {}
    filtered_dict = _create_remote_copy_args(original_dict)
    assert filtered_dict == expected_dict