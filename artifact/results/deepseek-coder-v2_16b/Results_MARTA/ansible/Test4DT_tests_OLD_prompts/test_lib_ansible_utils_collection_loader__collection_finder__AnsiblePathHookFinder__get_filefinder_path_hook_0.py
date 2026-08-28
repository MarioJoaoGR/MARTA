
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

def test_get_filefinder_path_hook():
    with patch('sys.path_hooks', [MagicMock()]):
        finder = _AnsiblePathHookFinder(collection_finder=None, pathctx="test_context")
        assert hasattr(finder, '_pathctx') and finder._pathctx == "test_context"
        assert hasattr(finder, '_collection_finder') and finder._collection_finder is None
        assert hasattr(finder, '_file_finder') and finder._file_finder is None


def test_filefinder_caching():
    with patch('sys.path_hooks', [MagicMock()]):
        finder = _AnsiblePathHookFinder(collection_finder=None, pathctx="test_context")
        assert hasattr(finder, '_pathctx') and finder._pathctx == "test_context"
        assert hasattr(finder, '_collection_finder') and finder._collection_finder is None
        assert hasattr(finder, '_file_finder') and finder._file_finder is None