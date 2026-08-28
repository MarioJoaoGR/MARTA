
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleInternalRedirectLoader, _get_collection_metadata, _nested_dict_get


def test_invalid_toplevel_package():
    with pytest.raises(ImportError):
        loader = _AnsibleInternalRedirectLoader('notansible.network.network_cli', [])
