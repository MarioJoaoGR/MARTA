
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys


def test_init_without_paths():
    finder = _AnsibleCollectionFinder()
    assert isinstance(finder._n_configured_paths, list), "Expected _n_configured_paths to be a list"
    assert len(finder._n_configured_paths) == 0, f"Expected no paths but got {len(finder._n_configured_paths)}"
