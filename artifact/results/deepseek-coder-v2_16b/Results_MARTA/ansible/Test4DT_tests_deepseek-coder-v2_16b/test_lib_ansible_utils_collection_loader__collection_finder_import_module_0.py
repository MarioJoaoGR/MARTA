
import pytest
import sys
from ansible.utils.collection_loader._collection_finder import import_module


def test_valid_module():
    module = import_module('os')
    assert hasattr(module, 'getcwd'), "Module 'os' should have a getcwd attribute"

def test_invalid_module():
    with pytest.raises(ImportError):
        import_module('nonexistentmodule')