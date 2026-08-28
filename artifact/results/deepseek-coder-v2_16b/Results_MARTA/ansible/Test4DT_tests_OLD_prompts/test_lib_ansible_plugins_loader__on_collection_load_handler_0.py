
import pytest
from unittest.mock import patch
from ansible.errors import AnsibleCollectionUnsupportedVersionError, AnsibleError
from ansible.plugins.loader import _get_collection_metadata, _does_collection_support_ansible_version
import ansible.config as C
import ansible.utils.display as display




def test_metadata_parsing_error():
    collection_meta = {}
    with patch('ansible.plugins.loader._get_collection_metadata', return_value=collection_meta):
        with pytest.raises(Exception):
            _on_collection_load_handler('mypackage', '/path/to/collections/mypackage')