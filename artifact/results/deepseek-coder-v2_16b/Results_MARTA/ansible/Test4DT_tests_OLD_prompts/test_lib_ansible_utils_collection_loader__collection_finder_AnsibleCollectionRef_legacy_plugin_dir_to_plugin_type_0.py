
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef



def test_invalid_ref_type():
    with pytest.raises(ValueError) as e:
        AnsibleCollectionRef('my_namespace.my_collection', 'subdir1.subdir2', 'mymodule', 'invalid_type')
    assert str(e.value) == "invalid collection ref_type: invalid_type"