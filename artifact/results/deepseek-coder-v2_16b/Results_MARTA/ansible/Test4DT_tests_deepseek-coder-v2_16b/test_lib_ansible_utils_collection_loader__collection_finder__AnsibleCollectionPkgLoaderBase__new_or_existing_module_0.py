
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase
import sys
from types import ModuleType

def test_edge_case():
    with pytest.raises(AttributeError):
        loader = _AnsibleCollectionPkgLoaderBase(None, [])
