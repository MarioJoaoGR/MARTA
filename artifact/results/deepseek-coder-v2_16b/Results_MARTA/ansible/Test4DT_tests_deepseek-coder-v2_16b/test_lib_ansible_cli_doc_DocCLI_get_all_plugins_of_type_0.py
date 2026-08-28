
import pytest
from ansible.cli.doc import DocCLI
import os

@pytest.fixture(scope="module")
def doc_cli():
    # Create a temporary directory for testing
    temp_dir = "/tmp/ansible_library"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    yield DocCLI(["dummy_args"])
    # Clean up the temporary directory after the test
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(temp_dir)


def test_find_plugins_with_invalid_path(doc_cli):
    # Test that find_plugins returns an empty set for an invalid path
    plugin_set = DocCLI.find_plugins('/invalid/path', True, 'module')
    assert isinstance(plugin_set, set), "Expected a set but got something else"
    assert len(plugin_set) == 0, "Expected no plugins but found some"

def test_find_plugins_with_no_plugins(doc_cli):
    # Test that find_plugins returns an empty set when there are no plugins of the specified type
    plugin_set = DocCLI.find_plugins('/tmp/ansible/library', True, 'module')
    assert isinstance(plugin_set, set), "Expected a set but got something else"
    assert len(plugin_set) == 0, "Expected no plugins but found some"