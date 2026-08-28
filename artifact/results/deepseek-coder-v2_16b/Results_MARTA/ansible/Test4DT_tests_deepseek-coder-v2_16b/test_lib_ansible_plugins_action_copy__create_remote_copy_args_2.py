
import pytest
from ansible.plugins.action.copy import _create_remote_copy_args



def test_no_extra_keys():
    original_dict = {'action': 'copy', 'source': '/local/path', 'destination': '/remote/path'}
    expected_output = {'action': 'copy', 'source': '/local/path', 'destination': '/remote/path'}
    assert _create_remote_copy_args(original_dict) == expected_output

def test_empty_dictionary():
    original_dict = {}
    expected_output = {}
    assert _create_remote_copy_args(original_dict) == expected_output