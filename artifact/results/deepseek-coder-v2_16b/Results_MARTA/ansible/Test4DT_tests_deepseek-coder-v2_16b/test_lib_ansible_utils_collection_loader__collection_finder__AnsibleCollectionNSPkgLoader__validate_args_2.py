
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionNSPkgLoader


def test_invalid_input():
    with pytest.raises(ImportError):
        _AnsibleCollectionNSPkgLoader('not_ansible.collections')

def test_edge_case_none():
    with pytest.raises(AttributeError):
        loader = _AnsibleCollectionNSPkgLoader(None)