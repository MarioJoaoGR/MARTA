
import json
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

def test_invalid_inputs():
    with patch('httpie.config.BaseConfigDict.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            config = BaseConfigDict(path=Path('/tmp/test_config'))
