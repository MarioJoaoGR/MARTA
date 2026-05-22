
from httpie.utils import split_iterable
from unittest.mock import patch
import pytest

def test_edge_case():
    with patch('httpie.utils.split_iterable', autospec=True) as mock_split:
        # Mock the behavior of split_iterable to return empty lists for None input
        mock_split.return_value = ([], [])
    
        # Test case 1: None input
        with pytest.raises(TypeError):
            result = split_iterable(None, lambda x: True)
