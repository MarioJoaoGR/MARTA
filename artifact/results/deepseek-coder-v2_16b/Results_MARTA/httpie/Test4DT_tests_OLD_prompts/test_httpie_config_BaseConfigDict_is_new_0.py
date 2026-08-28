
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock, mock_open
import json
from httpie.config import BaseConfigDict

@pytest.fixture
def config():
    return BaseConfigDict(path=Path('/some/file/path'))

def test_is_new(config):
    with patch('builtins.open', mock_open()) as m:
        assert config.is_new() == True

