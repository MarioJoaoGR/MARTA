
import pytest
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata
from unittest.mock import patch, MagicMock

# Test retrieval of valid collection metadata
def test_valid_collection_metadata():
    with patch('ansible.utils.collection_loader._collection_finder._get_collection_metadata') as mock_get:
        mock_get.return_value = {'key': 'value'}
        result = _get_collection_metadata('my_namespace.my_collection')
        assert result == {'key': 'value'}
        mock_get.assert_called_once_with('my_namespace.my_collection')

# Test raising ValueError for invalid type input
def test_invalid_type():
    with pytest.raises(ValueError) as e:
        _get_collection_metadata(12345)
    assert str(e.value) == 'collection_name must be a non-empty string of the form namespace.collection'

# Test raising ValueError for collection name with incorrect format
def test_invalid_format():
    with pytest.raises(ValueError) as e:
        _get_collection_metadata('my_namespace')
    assert str(e.value) == 'collection_name must be a non-empty string of the form namespace.collection'
