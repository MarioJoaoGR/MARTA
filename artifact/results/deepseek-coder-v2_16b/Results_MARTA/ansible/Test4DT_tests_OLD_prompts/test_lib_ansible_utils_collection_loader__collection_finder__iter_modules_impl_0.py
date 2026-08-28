
import pytest
import os
from unittest.mock import patch
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl

@pytest.fixture(autouse=True)
def mock_os_isdir():
    with patch('os.path.isdir', return_value=False):
        yield

def test_valid_case():
    paths = ['/path/to/module1', '/path/to/module2']
    result = list(_iter_modules_impl(paths))
    assert len(result) == 0, "Expected no modules or packages to be found"

def test_edge_case():
    paths = ['/path/to/module1', '/path/to/module2']
    result = list(_iter_modules_impl(paths))
    assert len(result) == 0, "Expected no modules or packages to be found"

def test_invalid_input():
    paths = ['/path/to/module1', '/path/to/module2']
    result = list(_iter_modules_impl(paths))
    assert len(result) == 0, "Expected no modules or packages to be found"
