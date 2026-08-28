
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleInternalRedirectLoader, _get_collection_metadata
from unittest.mock import patch
import sys
import importlib

@pytest.fixture
def valid_loader():
    return _AnsibleInternalRedirectLoader('ansible.network.network_cli', [])

@pytest.fixture
def invalid_loader():
    with pytest.raises(ImportError):
        yield _AnsibleInternalRedirectLoader('invalid.module.name', [])

@pytest.fixture
def missing_redirect_loader():
    with pytest.raises(ValueError):
        yield _AnsibleInternalRedirectLoader('ansible.builtin', [])



def test_missing_redirect():
    with pytest.raises(ValueError) as excinfo:
        _AnsibleInternalRedirectLoader('ansible.builtin', []).__init__('ansible.builtin', [])
    assert str(excinfo.value) == "unable to locate collection ansible.builtin"