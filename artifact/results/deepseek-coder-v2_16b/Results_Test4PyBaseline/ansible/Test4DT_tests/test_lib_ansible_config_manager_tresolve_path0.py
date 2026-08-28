# Module: ansible.config.manager
import pytest
import os
from ansible.config.manager import resolve_path

# Mock the unfrackpath function for testing purposes
def mock_unfrackpath(path, follow=False, basedir=None):
    if '{{CWD}}' in path:
        path = path.replace('{{CWD}}', os.getcwd())
    return os.path.normpath(os.path.join(basedir or os.getcwd(), path))

# Replace the actual unfrackpath function with the mock for testing
resolve_path.__wrapped__ = mock_unfrackpath

@pytest.mark.parametrize("input_path, expected", [
    ('{{CWD}}/data/file.txt', os.getcwd() + '/data/file.txt'),
    ('/home/user/project', '/home/user/project'),
    ('{{CWD}}/data/file.txt', os.getcwd() + '/data/file.txt'),
    (os.path.join(os.getcwd(), 'data/file.txt'), os.getcwd() + '/data/file.txt')
])
def test_resolve_path(input_path, expected):
    assert resolve_path(input_path) == expected
