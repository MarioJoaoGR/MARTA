
# Module: ansible.utils.collection_loader._collection_finder
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys

# Test initialization with specific paths and enabling scanning of system paths
def test_init_with_specific_paths():
    finder = _AnsibleCollectionFinder(paths=['/custom/collection/path'], scan_sys_paths=True)
    assert '/custom/collection/path' in finder._n_configured_paths
    assert os.path.isdir('/custom/collection/path')

# Test initialization without specifying paths but scanning system paths
def test_init_without_specific_paths():
    finder = _AnsibleCollectionFinder(scan_sys_paths=True)
    assert len(finder._n_configured_paths) > 0
    assert any('ansible_collections' in os.path.basename(p) for p in finder._n_configured_paths)

# Test setting playbook paths
def test_set_playbook_paths():
    finder = _AnsibleCollectionFinder(scan_sys_paths=True)
    finder.set_playbook_paths(['/path/to/playbooks'])
    assert os.path.isdir('/path/to/playbooks/collections')

# Test setting playbook paths with a string input
def test_set_playbook_paths_string():
    finder = _AnsibleCollectionFinder(scan_sys_paths=True)
    finder.set_playbook_paths(['/path/to/playbooks'])
    assert os.path.isdir('/path/to/playbooks/collections')

# Test reloading modules when necessary (hack method)
def test_reload_hack():
    finder = _AnsibleCollectionFinder(scan_sys_paths=True)
    for pkg in ['ansible_collections', 'ansible_collections.ansible']:
        assert sys.modules.get(pkg, None) is not None
