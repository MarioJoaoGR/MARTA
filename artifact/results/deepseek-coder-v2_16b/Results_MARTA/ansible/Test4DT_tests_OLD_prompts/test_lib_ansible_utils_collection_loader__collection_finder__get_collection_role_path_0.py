
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _get_collection_role_path



def test_unqualified_without_collection_list():
    with patch('ansible.utils.collection_loader._collection_finder._get_collection_resource_path', return_value=None):
        result = _get_collection_role_path('my_role')
        assert result is None