
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys

# Test initialization with specific paths and scanning system paths
def test_init_with_specific_paths():
    finder = _AnsibleCollectionFinder(paths=['/custom/collection/path'], scan_sys_paths=True)
    assert '/custom/collection/path' in finder._n_configured_paths, f"Expected path not found: {finder._n_configured_paths}"
    assert os.path.expanduser('~') not in finder._n_configured_paths  # Ensure home directory is not included

# Test initialization without specifying paths but scanning system paths
def test_init_without_specifying_paths():
    initial_sys_path = sys.path[:]  # Store the initial system path for comparison later
    finder = _AnsibleCollectionFinder(scan_sys_paths=True)
    assert os.path.expanduser('~') in finder._n_configured_paths, f"Expected home directory to be included but found: {finder._n_configured_paths}"  # Home directory should be included if scanning system paths
    assert initial_sys_path != sys.path, "System path was not modified by adding its own directories."  # Ensure the system path has been modified by adding its own directories

# Test initialization with a single-element list of paths and scanning system paths
def test_init_with_single_element_list():
    finder = _AnsibleCollectionFinder(paths=['/path/to/collection'], scan_sys_paths=True)
    assert '/path/to/collection' in finder._n_configured_paths, f"Expected path not found: {finder._n_configured_paths}"
    assert os.path.expanduser('~') not in finder._n_configured_paths  # Ensure home directory is not included

# Test initialization with invalid paths (non-existent directories)
def test_init_with_invalid_paths():
    with pytest.raises(TypeError):
        _AnsibleCollectionFinder(paths=['/nonexistent/path'])

# Test the method _reload_hack to ensure it reloads a module if already imported
def test_reload_hack():
    fullname = 'some.module'
    assert fullname not in sys.modules  # Ensure the module is not yet imported
    finder = _AnsibleCollectionFinder()
    finder._reload_hack(fullname)
    assert fullname in sys.modules, f"Expected {fullname} to be reloaded or imported but found: {sys.modules}"  # Ensure the module has been reloaded or imported after calling _reload_hack
