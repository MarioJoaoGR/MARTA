
import pytest
from isort.settings import Config

def test_config_init_with_none():
    """Test that Config can be initialized with None."""
    config = Config(config=None)
    assert isinstance(config, Config)
