
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase
import os


def test_invalid_fullname():
    with pytest.raises(ImportError):
        _AnsibleCollectionPkgLoaderBase(fullname='invalid.namespace.module')

