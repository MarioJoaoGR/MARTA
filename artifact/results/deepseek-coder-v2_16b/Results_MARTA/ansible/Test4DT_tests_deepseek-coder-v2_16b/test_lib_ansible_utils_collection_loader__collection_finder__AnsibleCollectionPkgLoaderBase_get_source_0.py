
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase




def test_get_source_invalid_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.somodule', path_list=['/path/to/collection'])
    with pytest.raises(ValueError):
        source_code = loader.get_source('invalid.fullname')