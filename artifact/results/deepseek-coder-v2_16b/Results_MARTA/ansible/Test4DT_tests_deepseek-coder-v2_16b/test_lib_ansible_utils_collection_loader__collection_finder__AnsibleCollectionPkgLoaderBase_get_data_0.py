
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase


def test_invalid_fullname():
    with pytest.raises(ImportError):
        _AnsibleCollectionPkgLoaderBase('invalid.fullname')