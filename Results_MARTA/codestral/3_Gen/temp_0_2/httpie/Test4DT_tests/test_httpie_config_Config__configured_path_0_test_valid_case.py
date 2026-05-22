
import pytest
from unittest.mock import patch, MagicMock
from httpie.config import Config

@pytest.fixture(autouse=True)
def mock_config():
    with patch('httpie.config.Config.FILENAME', 'test_config.json'):
        with patch('httpie.config.Config.DEFAULTS', {'default_options': []}):
            yield Config()

def test_valid_case():
    config = Config()
    assert config.FILENAME == 'test_config.json'
    assert config.DEFAULTS == {'default_options': []}
