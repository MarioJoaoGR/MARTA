
import pytest
from unittest.mock import patch, MagicMock
from httpie.config import Config

def test_invalid_input():
    with patch('httpie.config.Config', spec=True) as mock_config:
        # Create an instance of the Config class
        config = Config()
        
        # Mock the get method to raise a TypeError when called
        mock_get = MagicMock(side_effect=TypeError("Invalid type provided"))
        with patch.object(Config, 'get', new=mock_get):
            # Call developer_mode which should call get and raise TypeError
            with pytest.raises(TypeError) as excinfo:
                config.developer_mode()
                
    assert str(excinfo.value) == "Invalid type provided"
