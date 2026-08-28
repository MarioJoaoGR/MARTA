
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test_valid_input():
    with pytest.raises(TypeError):
        loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.somodule')
