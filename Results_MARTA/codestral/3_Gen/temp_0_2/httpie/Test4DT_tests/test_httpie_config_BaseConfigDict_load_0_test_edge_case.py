
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

def test_edge_case():
    with patch('httpie.config.read_raw_config', return_value=None):
        config = BaseConfigDict(path=None)
        assert config.path is None
