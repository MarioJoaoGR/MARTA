
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase
import os

# Helper function to convert strings to bytes for compatibility with Python 3 on Windows
def to_bytes(path):
    if isinstance(path, str):
        return path.encode('utf-8')
    return path

def to_native(path):
    if isinstance(path, bytes):
        return path.decode('utf-8')
    return path

# Test cases for _get_subpackage_search_paths method
@pytest.mark.parametrize("candidate_paths, expected", [
    (['/valid/path1', '/valid/path2'], ['/valid/path1', '/valid/path2']),  # Both paths are valid directories
    (['/valid/path1', 'invalid/path'], ['/valid/path1']),                # One invalid path
    ([], []),                                                            # No candidate paths
])
def test_get_subpackage_search_paths(candidate_paths, expected):
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.dummy')  # Dummy initialization to run the method
    result = loader._get_subpackage_search_paths([to_native(p) for p in candidate_paths])
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"
