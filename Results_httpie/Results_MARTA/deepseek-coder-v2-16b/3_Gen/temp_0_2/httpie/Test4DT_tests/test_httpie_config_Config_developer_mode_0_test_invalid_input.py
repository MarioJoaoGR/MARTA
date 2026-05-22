
import pytest
from unittest.mock import patch, MagicMock
from httpie.config import Config

def test_invalid_input():
    with patch('httpie.config.Config.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            config = Config()
