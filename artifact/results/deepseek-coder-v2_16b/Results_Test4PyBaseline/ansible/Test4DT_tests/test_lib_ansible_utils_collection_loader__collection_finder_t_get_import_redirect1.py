
# Module: ansible.utils.collection_loader._collection_finder
# test_collection_loader.py
from ansible.utils.collection_loader._collection_finder import _get_import_redirect

def test_empty_collection_meta_dict():
    # Test when collection_meta_dict is empty
    result = _get_import_redirect({}, 'nonexistent')
    assert result is None, f"Expected None, but got {result}"

def test_fullname_not_in_import_redirection():
    # Test when fullname does not exist in import_redirection
    data = {'import_redirection': {'mypackage': {'redirect': 'newpackage'}}}
    result = _get_import_redirect(data, 'nonexistent')
    assert result is None, f"Expected None, but got {result}"

def test_nested_dict_get_usage():
    # Test the usage of _nested_dict_get within _get_import_redirect
    data = {'import_redirection': {'mypackage': {'redirect': 'newpackage'}}}
    result = _get_import_redirect(data, 'mypackage')
    assert result == 'newpackage', f"Expected 'newpackage', but got {result}"
