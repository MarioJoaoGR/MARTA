
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys


def test_default_initialization():
    finder = _AnsibleCollectionFinder()
    assert isinstance(finder, _AnsibleCollectionFinder), "Instance should be an instance of _AnsibleCollectionFinder"
    assert finder._n_configured_paths == [], "Expected empty list for configured paths when initialized without arguments"


