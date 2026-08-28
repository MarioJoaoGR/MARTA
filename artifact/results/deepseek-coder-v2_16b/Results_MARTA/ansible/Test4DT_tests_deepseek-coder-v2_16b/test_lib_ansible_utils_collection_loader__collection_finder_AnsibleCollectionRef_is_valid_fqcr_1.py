
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef




def test_error_case_4():
    with pytest.raises(ValueError) as e:
        collection_ref = AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', 'mymodule', 'invalid_type')
    assert str(e.value) == 'invalid collection ref_type: invalid_type'