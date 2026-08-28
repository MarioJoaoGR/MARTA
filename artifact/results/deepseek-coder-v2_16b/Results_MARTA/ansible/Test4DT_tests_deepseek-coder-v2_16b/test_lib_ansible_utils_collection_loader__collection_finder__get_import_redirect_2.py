
import pytest
from ansible.utils.collection_loader._collection_finder import _get_import_redirect

# Test for valid input scenario
def test_valid_input():
    collection_meta = {'import_redirection': {'mypackage.module': {'redirect': 'newpackage'}}}
    assert _get_import_redirect(collection_meta, 'mypackage.module') == 'newpackage'

# Test for empty metadata scenario
def test_empty_metadata():
    collection_meta = {}
    assert _get_import_redirect(collection_meta, 'mypackage.module') is None

# Test for fullname not found in collection metadata scenario
def test_fullname_not_found():
    collection_meta = {'import_redirection': {'anotherpackage.module': {'redirect': 'differentpackage'}}}
    assert _get_import_redirect(collection_meta, 'mypackage.module') is None
