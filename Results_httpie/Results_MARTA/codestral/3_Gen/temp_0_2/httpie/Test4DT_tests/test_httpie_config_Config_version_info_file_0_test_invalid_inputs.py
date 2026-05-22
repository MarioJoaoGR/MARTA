
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from httpie.config import Config

def test_invalid_inputs():
    with patch('httpie.config.Config.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            config = Config()
