
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test_edge_case():
    with pytest.raises(AttributeError) as excinfo:
        loader = _AnsibleCollectionPkgLoaderBase(None, [])
    assert str(excinfo.value) == "'NoneType' object has no attribute 'split'"

def test_invalid_input():
    try:
        loader = _AnsibleCollectionPkgLoaderBase('invalid.fullname')
    except Exception as e:
        assert str(e) == "this loader can only load packages from the ansible_collections package, not invalid.fullname"
