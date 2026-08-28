
import pytest
from unittest.mock import patch
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata


def test_invalid_collection_name_type():
    with pytest.raises(ValueError):
        _get_collection_metadata(12345)  # Passing an integer instead of a string

def test_invalid_collection_name_format():
    with pytest.raises(ValueError):
        _get_collection_metadata('my_namespace')  # Missing part after dot

def test_nonexistent_collection():
    with pytest.raises(ValueError):
        _get_collection_metadata('nonexistent.namespace')  # Non-existent collection

def test_empty_collection_name():
    with pytest.raises(ValueError):
        _get_collection_metadata('')  # Passing an empty string