
from isort.deprecated.finders import PathFinder
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_config():
    config = MagicMock()
    config.virtual_env = None
    config.conda_env = None
    return config

@pytest.fixture
def pathfinder(mock_config):
    return PathFinder(config=mock_config)

def test_find_module_not_found(pathfinder):
    with patch('os.path.exists', return_value=False):
        assert pathfinder.find("non_existent_module") is None
