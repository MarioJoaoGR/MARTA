
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

# Test initialization of AnsiblePathHookFinder
@pytest.fixture(name="finder")
def fixture_finder():
    collection_finder = MagicMock()
    pathctx = "test_pathctx"
    return _AnsiblePathHookFinder(collection_finder, pathctx)


# Test __repr__ method of AnsiblePathHookFinder
def test_ansible_path_hook_finder_repr():
    collection_finder = MagicMock()
    pathctx = "test_pathctx"
    finder = _AnsiblePathHookFinder(collection_finder, pathctx)
    assert repr(finder) == f"{finder.__class__.__name__}(path='{pathctx}')"

# Test iter_modules method of AnsiblePathHookFinder