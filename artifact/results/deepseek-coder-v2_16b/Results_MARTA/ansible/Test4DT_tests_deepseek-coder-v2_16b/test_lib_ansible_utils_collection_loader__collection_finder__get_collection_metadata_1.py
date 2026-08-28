
import pytest
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata


def test_invalid_collection_name_type():
    with pytest.raises(ValueError) as e:
        _get_collection_metadata(12345)
    assert str(e.value) == "collection_name must be a non-empty string of the form namespace.collection"

def test_invalid_collection_name_format():
    with pytest.raises(ValueError) as e:
        _get_collection_metadata('my_namespace')
    assert str(e.value) == "collection_name must be a non-empty string of the form namespace.collection"

def test_nonexistent_collection():
    collection_name = 'nonexistent.namespace'
    with pytest.raises(ValueError) as e:
        _get_collection_metadata(collection_name)
    assert str(e.value) == f"unable to locate collection {collection_name}"

def test_empty_collection_name():
    with pytest.raises(ValueError) as e:
        _get_collection_metadata('')
    assert str(e.value) == "collection_name must be a non-empty string of the form namespace.collection"