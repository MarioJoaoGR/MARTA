# Module: ansible.utils.collection_loader._collection_finder
# test_collection_loader.py
from ansible.utils.collection_loader._collection_finder import _get_import_redirect

def test_basic_usage():
    data = {'import_redirection': {'mypackage': {'redirect': 'newpackage'}}}
    result = _get_import_redirect(data, 'mypackage')
    assert result == 'newpackage', f"Expected 'newpackage', but got {result}"

def test_empty_dict():
    empty_dict = {}
    result = _get_import_redirect(empty_dict, 'nonexistent')
    assert result is None, f"Expected None, but got {result}"

def test_no_redirect_found():
    data = {'import_redirection': {'mypackage': {'redirect': 'newpackage'}}}
    result = _get_import_redirect(data, 'anotherpackage')
    assert result is None, f"Expected None, but got {result}"

def test_different_structure():
    data = {
        'config': {
            'import_redirection': {'mypackage': {'redirect': 'newpackage'}}
        }
    }
    result = _get_import_redirect(data['config'], 'mypackage')
    assert result == 'newpackage', f"Expected 'newpackage', but got {result}"

def test_handling_edge_cases():
    data = {'import_redirection': {}}
    result = _get_import_redirect(data, 'nonexistent')
    assert result is None, f"Expected None, but got {result}"
