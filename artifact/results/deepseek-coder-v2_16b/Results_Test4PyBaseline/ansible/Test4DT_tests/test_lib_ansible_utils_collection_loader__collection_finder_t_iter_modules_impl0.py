
import os
from ansible.utils.collection_loader._collection_finder import _iter_modules_impl

def test_basic_usage():
    paths = ['/path/to/module1', '/path/to/module2']
    results = list(_iter_modules_impl(paths))
    assert len(results) == 2, "Expected two results"
    assert ('module1', False) in results, "Expected 'module1' to be found without prefix"
    assert ('module2', False) in results, "Expected 'module2' to be found without prefix"

def test_with_prefix():
    paths = ['/path/to/module1', '/path/to/module2']
    prefix = 'my_prefix_'
    results = list(_iter_modules_impl(paths, prefix))
    assert len(results) == 2, "Expected two results with prefix"
    assert ('my_prefix_module1', False) in results, "Expected 'my_prefix_module1' to be found with prefix"
    assert ('my_prefix_module2', False) in results, "Expected 'my_prefix_module2' to be found with prefix"

def test_using_different_paths():
    paths = ['/another/path/to/module1', '/another/path/to/module2']
    results = list(_iter_modules_impl(paths))
    assert len(results) == 2, "Expected two results with different paths"
    assert ('module1', False) in results, "Expected 'module1' to be found from another path"
    assert ('module2', False) in results, "Expected 'module2' to be found from another path"

def test_with_longer_paths_and_custom_prefix():
    paths = ['/long/path/to/module1', '/long/path/to/module2']
    prefix = 'custom_'
    results = list(_iter_modules_impl(paths, prefix))
    assert len(results) == 2, "Expected two results with longer paths and custom prefix"
    assert ('custom_module1', False) in results, "Expected 'custom_module1' to be found with custom prefix"
    assert ('custom_module2', False) in results, "Expected 'custom_module2' to be found with custom prefix"
