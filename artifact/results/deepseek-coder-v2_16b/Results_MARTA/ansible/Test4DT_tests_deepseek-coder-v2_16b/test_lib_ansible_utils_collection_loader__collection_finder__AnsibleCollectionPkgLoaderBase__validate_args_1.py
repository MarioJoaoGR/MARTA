
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase


def test_none_input():
    with pytest.raises(AttributeError):
        loader = _AnsibleCollectionPkgLoaderBase(None)