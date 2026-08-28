
import pytest
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl
import os



def test_invalid_paths():
    paths = ['/nonexistent/path']
    result = list(_iter_modules_impl(paths))
    assert len(result) == 0, "Expected no results for invalid path"