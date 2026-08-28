# Module: ansible.modules.lineinfile
import pytest
from unittest.mock import MagicMock
import os
import tempfile
from ansible.modules.lineinfile import write_changes

# Mock Ansible module object and parameters for testing
@pytest.fixture
def mock_module():
    module = MagicMock()
    module.params = {}
    return module

def test_write_changes_basic(mock_module):
    b_lines = [b"line1", b"line2"]
    dest = "test_dest"
    mock_module.params = {'unsafe_writes': False}
    
    write_changes(mock_module, b_lines, dest)
    
    # Add assertions to check if the function has performed as expected
    assert os.path.exists(tempfile.gettempdir() + "/ansible_tmp/lineinfile/tmp_*")
    with open(tempfile.gettempdir() + "/ansible_tmp/lineinfile/tmp_*", 'rb') as f:
        content = f.readlines()
        assert content == b_lines

def test_write_changes_with_validate(mock_module):
    b_lines = [b"line1", b"line2"]
    dest = "test_dest"
    mock_module.params = {'unsafe_writes': False, 'validate': "my_validation_script.py"}
    
    write_changes(mock_module, b_lines, dest)
    
    # Add assertions to check if the function has performed as expected
    assert os.path.exists(tempfile.gettempdir() + "/ansible_tmp/lineinfile/tmp_*")
    with open(tempfile.gettempdir() + "/ansible_tmp/lineinfile/tmp_*", 'rb') as f:
        content = f.readlines()
        assert content == b_lines

def test_write_changes_with_unsafe_writes(mock_module):
    b_lines = [b"line1", b"line2"]
    dest = "test_dest"
    mock_module.params = {'unsafe_writes': True}
    
    write_changes(mock_module, b_lines, dest)
    
    # Add assertions to check if the function has performed as expected
    assert os.path.exists(tempfile.gettempdir() + "/ansible_tmp/lineinfile/tmp_*")
    with open(tempfile.gettempdir() + "/ansible_tmp/lineinfile/tmp_*", 'rb') as f:
        content = f.readlines()
        assert content == b_lines

def test_write_changes_with_invalid_validate(mock_module):
    b_lines = [b"line1", b"line2"]
    dest = "test_dest"
    mock_module.params = {'unsafe_writes': False, 'validate': "invalid_validation_script"}
    
    with pytest.raises(Exception) as e:
        write_changes(mock_module, b_lines, dest)
        
    assert str(e.value) == 'failed to validate: rc:1 error:No such file or directory'
