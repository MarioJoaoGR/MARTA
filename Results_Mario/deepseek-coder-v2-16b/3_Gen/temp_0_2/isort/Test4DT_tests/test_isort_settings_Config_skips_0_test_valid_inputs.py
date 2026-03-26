
import pytest
from isort.settings import _Config

@pytest.fixture
def valid_config():
    return _Config(quiet=True)

def test_valid_inputs(valid_config):
    assert isinstance(valid_config, _Config)
    assert valid_config.quiet == True
