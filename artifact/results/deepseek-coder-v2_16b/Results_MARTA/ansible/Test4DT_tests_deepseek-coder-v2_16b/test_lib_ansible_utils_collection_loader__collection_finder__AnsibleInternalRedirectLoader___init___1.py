
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleInternalRedirectLoader, _get_collection_metadata


def test_invalid_module_import():
    # Test an invalid module import (wrong top-level package)
    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader('notansible.network.network_cli', [])
