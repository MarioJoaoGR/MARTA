
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionNSPkgLoader


def test_invalid_input():
    with pytest.raises(ImportError):
        loader = _AnsibleCollectionNSPkgLoader(fullname='not_valid')