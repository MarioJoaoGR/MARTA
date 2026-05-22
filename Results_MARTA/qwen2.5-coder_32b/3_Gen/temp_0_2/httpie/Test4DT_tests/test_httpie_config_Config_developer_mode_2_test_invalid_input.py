
import pytest
from unittest.mock import patch, MagicMock
from httpie.config import Config

def test_invalid_input():
    with patch('httpie.config.Config', spec=Config):
        config = Config()
        with pytest.raises(TypeError):
            config.developer_mode("incorrect type")
