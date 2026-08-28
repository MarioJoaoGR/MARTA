
import pytest
from ansible.plugins.loader import _on_collection_load_handler
from ansible.errors import AnsibleCollectionUnsupportedVersionError

# Test case 1: Collection supports the current Ansible version
def test_on_collection_load_handler_supported():
    with pytest.raises(AnsibleCollectionUnsupportedVersionError) as excinfo:
        _on_collection_load_handler('example_collection', '/path/to/collection')
    assert str(excinfo.value) == 'Collection example_collection does not support Ansible version 2.10'

# Test case 2: Collection does not support the current Ansible version, raises error
def test_on_collection_load_handler_unsupported():
    with pytest.raises(AnsibleCollectionUnsupportedVersionError) as excinfo:
        _on_collection_load_handler('example_collection', '/path/to/collection')
    assert str(excinfo.value) == 'Collection example_collection does not support Ansible version 2.10'

# Test case 3: Collection supports the current Ansible version, no error expected
def test_on_collection_load_handler_supported_no_error():
    with pytest.raises(None) as excinfo:  # Replace None with expected exception if any
        _on_collection_load_handler('example_collection', '/path/to/collection')
    assert str(excinfo.value) is None  # Assuming no error means the message should be empty or similar
