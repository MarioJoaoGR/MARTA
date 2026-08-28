
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader
import os
import importlib

@pytest.fixture(scope="module")
def loader():
    return _AnsibleCollectionPkgLoader()


def test_edge_case_none():
    with pytest.raises(TypeError):
        loader = _AnsibleCollectionPkgLoader()