
# Module: ansible.utils.collection_loader._collection_finder
# test_collection_loader.py
from ansible.utils.collection_loader._collection_finder import _get_import_redirect

def test_empty_meta_dict():
    data = {}
    result = _get_import_redirect(data, 'mypackage')
    assert result is None, f"Expected None for empty dictionary, but got {result}"

def test_fullname_not_found():
    data = {'import_redirection': {'nonexistentpackage': {'redirect': 'newpackage'}}}
    result = _get_import_redirect(data, 'mypackage')
    assert result is None, f"Expected None when fullname not found, but got {result}"

def test_correct_fullname():
    data = {'import_redirection': {'mypackage': {'redirect': 'newpackage'}}}
    result = _get_import_redirect(data, 'mypackage')
    assert result == 'newpackage', f"Expected 'newpackage' for correct fullname, but got {result}"

def test_incorrect_structure():
    data = {
        'config': {
            'import_redirection': {'mypackage': {'redirect': 'newpackage'}}
        }
    }
    result = _get_import_redirect(data['config'], 'mypackage')
    assert result == 'newpackage', f"Expected 'newpackage' for incorrect structure, but got {result}"
