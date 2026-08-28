
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader


def test_none_case():
    with pytest.raises(AttributeError):
        loader = _AnsibleCollectionPkgLoader(None)