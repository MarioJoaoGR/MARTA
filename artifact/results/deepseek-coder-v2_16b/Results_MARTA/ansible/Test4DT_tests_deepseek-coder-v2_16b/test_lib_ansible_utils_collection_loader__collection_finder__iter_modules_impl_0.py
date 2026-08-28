
import pytest
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl
import os

# Test for basic functionality without any prefix
def test__iter_modules_impl_basic():
    paths = ['/path/to/module1', '/path/to/module2']
    expected_results = [('module1', True), ('module2', False)]
    
    results = list(_iter_modules_impl(paths))
    
    assert len(results) == len(expected_results)
    for result, expected in zip(results, expected_results):
        assert result == expected

# Test for functionality with a specified prefix
def test__iter_modules_impl_with_prefix():
    paths = ['/path/to/module1', '/path/to/module2']
    prefix = 'myprefix_'
    expected_results = [('myprefix_module1', True), ('myprefix_module2', False)]
    
    results = list(_iter_modules_impl(paths, prefix))
    
    assert len(results) == len(expected_results)
    for result, expected in zip(results, expected_results):
        assert result == expected

# Test for default behavior when no prefix is provided
def test__iter_modules_impl_default_prefix():
    paths = ['/path/to/module1', '/path/to/module2']
    expected_results = [('module1', True), ('module2', False)]
    
    results = list(_iter_modules_impl(paths))
    
    assert len(results) == len(expected_results)
    for result, expected in zip(results, expected_results):
        assert result == expected
