
import pytest
from httpie.context import Environment, DEFAULT_CONFIG_DIR
from unittest.mock import patch
from pathlib import Path

@pytest.fixture
def valid_environment():
    return Environment(config_dir=Path('/tmp/config'))

def test_valid_inputs(valid_environment):
    with patch('httpie.context.DEFAULT_CONFIG_DIR', Path('/tmp/config')):
        assert valid_environment.config_dir == Path('/tmp/config')
