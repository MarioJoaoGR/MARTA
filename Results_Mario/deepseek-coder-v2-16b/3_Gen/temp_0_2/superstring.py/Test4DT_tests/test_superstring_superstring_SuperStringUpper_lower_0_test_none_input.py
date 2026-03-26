
import pytest
from unittest.mock import patch
from superstring.superstring import SuperStringUpper

def test_none_input():
    with patch('superstring.superstring.SuperStringUpper', autospec=True) as mock_class:
        # Arrange
        mock_instance = mock_class.return_value
        s = SuperStringUpper(None)
        
        # Act and Assert
        assert s._base is None
