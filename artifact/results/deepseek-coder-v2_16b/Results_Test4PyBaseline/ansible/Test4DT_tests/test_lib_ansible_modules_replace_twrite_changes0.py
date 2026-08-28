# Module: ansible.modules.replace
import pytest
from ansible.modules.replace import write_changes
from unittest.mock import MagicMock
import os
import tempfile

# Mock AnsibleModule for testing
@pytest.fixture
def mock_ansible_module():
    module = MagicMock()
    module.params = {'validate': None, 'unsafe_writes': False, 'tmpdir': '/tmp'}
    return module

def test_write_changes_default(mock_ansible_module):
    write_changes(mock_ansible_module, b'example content', '/destination/path')
    assert os.path.exists('/tmp/tmpfile')
    with open('/tmp/tmpfile', 'rb') as f:
        assert f.read() == b'example content'

def test_write_changes_with_validation(mock_ansible_module):
    mock_ansible_module.params['validate'] = "echo %s > /dev/null"
    write_changes(mock_ansible_module, b'example content', '/destination/path')
    assert os.path.exists('/tmp/tmpfile')
    with open('/tmp/tmpfile', 'rb') as f:
        assert f.read() == b'example content'

def test_write_changes_with_validation_failure(mock_ansible_module):
    mock_ansible_module.params['validate'] = "false"  # Always fails validation
    with pytest.raises(SystemExit) as e:
        write_changes(mock_ansible_module, b'example content', '/destination/path')
    assert str(e.value) == '1'  # AnsibleModule failure should exit with code 1

def test_write_changes_with_unsafe_writes(mock_ansible_module):
    mock_ansible_module.params['unsafe_writes'] = True
    write_changes(mock_ansible_module, b'example content', '/destination/path')
    assert os.path.exists('/destination/path')
