# Module: ansible.utils.collection_loader._collection_finder
# test_collection_loader.py
from ansible.utils.collection_loader._collection_finder import _AnsibleInternalRedirectLoader
import pytest

def test_valid_fullname_and_path_list():
    loader = _AnsibleInternalRedirectLoader('ansible.modules.my_module', ['path1', 'path2'])
    assert loader is not None, "Expected a non-None instance of _AnsibleInternalRedirectLoader"

def test_invalid_top_level_package_name():
    with pytest.raises(ImportError) as excinfo:
        loader = _AnsibleInternalRedirectLoader('notansible.modules.my_module', ['path1', 'path2'])
    assert str(excinfo.value) == "not interested", f"Expected ImportError for invalid top-level package, got {excinfo.value}"

def test_no_redirection():
    with pytest.raises(ImportError) as excinfo:
        loader = _AnsibleInternalRedirectLoader('ansible.modules.unrecognized_module', ['path1', 'path2'])
    assert str(excinfo.value) == "not redirected, go ask path_hook", f"Expected ImportError for no redirection, got {excinfo.value}"
