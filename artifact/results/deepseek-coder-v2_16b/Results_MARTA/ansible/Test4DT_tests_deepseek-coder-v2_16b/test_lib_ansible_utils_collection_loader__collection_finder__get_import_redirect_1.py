
import pytest
from ansible.utils.collection_loader._collection_finder import _get_import_redirect

# Test for valid input scenario
def test_valid_input():
    collection_meta = {'import_redirection': {'mypackage.module': {'redirect': 'newpackage'}}}
    assert _get_import_redirect(collection_meta, 'mypackage.module') == 'newpackage'

# Test for scenario where fullname is not in collection metadata
def test_missing_fullname():
    collection_meta = {'import_redirection': {'anotherpackage.module': {'redirect': 'differentpackage'}}}
    assert _get_import_redirect(collection_meta, 'mypackage.module') is None

# Test for scenario where collection metadata is empty
def test_empty_metadata():
    collection_meta = {}
    assert _get_import_redirect(collection_meta, 'mypackage.module') is None
