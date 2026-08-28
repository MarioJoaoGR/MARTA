
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Test for valid input scenario

# Test for edge case where fullname is None
def test_edge_case():
    with pytest.raises(AttributeError):
        loader = _AnsibleCollectionPkgLoaderBase(None)