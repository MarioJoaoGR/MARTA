
import pytest
from unittest.mock import patch, MagicMock
from httpie.config import Config

def test_error_handling():
    with patch('httpie.config.Config.__init__', side_effect=ValueError("Invalid directory")):
        with pytest.raises(ValueError):
            config = Config()
