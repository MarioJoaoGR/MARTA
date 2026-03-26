
import pytest
from isort.deprecated.finders import PathFinder
from unittest.mock import MagicMock

@pytest.fixture(scope="module")
def mock_config():
    config = MagicMock()
    config.virtual_env = None
    config.conda_env = None
    return config

def test_valid_case(mock_config):
    finder = PathFinder(config=mock_config)
    assert finder is not None
