
import pytest
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata


def test_invalid_collection_name_type():
    with pytest.raises(ValueError) as excinfo:
        _get_collection_metadata(12345)
    assert str(excinfo.value) == "collection_name must be a non-empty string of the form namespace.collection"

def test_invalid_collection_name_format():
    with pytest.raises(ValueError) as excinfo:
        _get_collection_metadata('my_namespace')
    assert str(excinfo.value) == "collection_name must be a non-empty string of the form namespace.collection"

def test_nonexistent_collection():
    with pytest.raises(ValueError) as excinfo:
        _get_collection_metadata('nonexistent.namespace')
    assert str(excinfo.value) == "unable to locate collection nonexistent.namespace"

def test_empty_collection_name():
    with pytest.raises(ValueError) as excinfo:
        _get_collection_metadata('')
    assert str(excinfo.value) == "collection_name must be a non-empty string of the form namespace.collection"