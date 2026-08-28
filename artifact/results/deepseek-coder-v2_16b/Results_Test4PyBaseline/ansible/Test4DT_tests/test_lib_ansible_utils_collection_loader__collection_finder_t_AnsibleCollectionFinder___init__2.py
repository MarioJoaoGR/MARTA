
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys

# Test initialization with specific paths and enabling system path scanning
def test_init_with_specific_paths():
    finder = _AnsibleCollectionFinder(paths=['/custom/collection/path'], scan_sys_paths=True)
    assert isinstance(finder, _AnsibleCollectionFinder), "Instance should be of type _AnsibleCollectionFinder"