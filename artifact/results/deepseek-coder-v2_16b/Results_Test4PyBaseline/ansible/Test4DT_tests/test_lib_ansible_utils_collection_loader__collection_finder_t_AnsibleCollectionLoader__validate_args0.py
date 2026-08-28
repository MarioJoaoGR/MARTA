
# Module: ansible.utils.collection_loader._collection_finder
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionLoader

# Test case 1: Valid collection name with at least four parts
def test_validate_args_valid():
    loader = _AnsibleCollectionLoader(fullname='ansible_collections.example.subcollection')
    try:
        loader._validate_args()
    except ValueError as e:
        pytest.fail(f"Unexpected ValueError raised: {e}")

# Test case 2: Invalid collection name with less than four parts
def test_validate_args_invalid():
    loader = _AnsibleCollectionLoader(fullname='ansible_collections.example')
    with pytest.raises(ValueError) as excinfo:
        loader._validate_args()
    assert str(excinfo.value) == "this loader is only for sub-collection modules/packages, not ansible_collections.example"
