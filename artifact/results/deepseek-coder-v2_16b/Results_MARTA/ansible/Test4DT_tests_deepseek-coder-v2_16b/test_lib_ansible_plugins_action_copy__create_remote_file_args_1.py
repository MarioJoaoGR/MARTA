
import pytest
from ansible.plugins.action.copy import _create_remote_file_args

# Define a set of relevant file operation keys for testing
REAL_FILE_ARGS = {'path', 'owner', 'group', 'mode'}

@pytest.fixture(scope="module")
def module_args():
    return {
        'path': '/some/file/path',
        'owner': 'user1',
        'group': 'group1',
        'mode': '0644',
        'command': 'ls -l',  # Irrelevant key to test filtering
        'timeout': 120,      # Irrelevant key to test filtering
    }

def test_filtering_irrelevant_keys(module_args):
    filtered_args = _create_remote_file_args(module_args)
    assert 'command' not in filtered_args, "Expected irrelevant key 'command' to be filtered out."
    assert 'timeout' not in filtered_args, "Expected irrelevant key 'timeout' to be filtered out."
    assert len(filtered_args) == 4, "Expected exactly four keys after filtering."
