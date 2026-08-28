
import pytest
from unittest.mock import patch

# Assuming _get_import_redirect and _nested_dict_get are defined as per the provided function definition
def _get_import_redirect(collection_meta_dict, fullname):
    if not collection_meta_dict:
        return None
    return _nested_dict_get(collection_meta_dict, ['import_redirection', fullname, 'redirect'])

# Mock for testing purposes
def _nested_dict_get(data, keys):
    result = data
    for key in keys:
        if isinstance(result, dict) and key in result:
            result = result[key]
        else:
            return None
    return result

# Test cases
@pytest.mark.parametrize("collection_meta, fullname, expected", [
    ({'import_redirection': {'mypackage.module': {'redirect': 'newpackage'}}}, 'mypackage.module', 'newpackage'),
    ({}, 'mypackage.module', None),
    ({'import_redirection': {'anotherpackage.module': {'redirect': 'differentpackage'}}}, 'mypackage.module', None)
])
def test_get_import_redirect(collection_meta, fullname, expected):
    with patch('ansible.utils.collection_loader._collection_finder._nested_dict_get', side_effect=_nested_dict_get):
        assert _get_import_redirect(collection_meta, fullname) == expected
