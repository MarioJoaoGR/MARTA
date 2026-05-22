
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

@pytest.fixture(name="valid_config")
def fixture_valid_config():
    config = BaseConfigDict(path=Path('/some/file/path'))
    config.name = "TestApp"
    return config

def test_valid_inputs(valid_config):
    assert valid_config.name == "TestApp"
