# Module: ansible.plugins.action.copy
import pytest
from ansible.plugins.action import ActionModule as Am
import os

@pytest.fixture
def action_module():
    return Am()

# Test case for _remove_tempfile_if_content_defined when content is provided and non-None
def test_remove_tempfile_when_content_is_provided(action_module):
    content = "some data"
    tempfile_path = "/tmp/test_tempfile"
    with open(tempfile_path, 'w') as f:
        f.write(content)
    
    action_module._remove_tempfile_if_content_defined(content, tempfile_path)
    
    assert not os.path.exists(tempfile_path)

# Test case for _remove_tempfile_if_content_defined when content is None or not provided
def test_do_nothing_when_content_is_none(action_module):
    tempfile_path = "/tmp/test_tempfile"
    with open(tempfile_path, 'w') as f:
        f.write("some data")
    
    action_module._remove_tempfile_if_content_defined(None, tempfile_path)
    
    assert os.path.exists(tempfile_path)

# Test case for _remove_tempfile_if_content_defined when content is provided but empty string
def test_do_nothing_when_content_is_empty_string(action_module):
    tempfile_path = "/tmp/test_tempfile"
    with open(tempfile_path, 'w') as f:
        f.write("")
    
    action_module._remove_tempfile_if_content_defined("", tempfile_path)
    
    assert os.path.exists(tempfile_path)
