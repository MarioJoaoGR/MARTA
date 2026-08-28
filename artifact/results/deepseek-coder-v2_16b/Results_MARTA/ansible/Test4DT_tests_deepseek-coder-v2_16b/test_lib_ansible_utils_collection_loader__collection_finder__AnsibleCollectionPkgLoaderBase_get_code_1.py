
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase


def test_invalid_input():
    with pytest.raises(Exception):
        _AnsibleCollectionPkgLoaderBase('invalid.module', [])