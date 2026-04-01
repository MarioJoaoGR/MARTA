
import pytest
from isort.deprecated.finders import PathFinder
from unittest.mock import patch, MagicMock

@pytest.fixture(autouse=True)
def setup_pathfinder():
    config = MagicMock()
    config.virtual_env = None
    config.conda_env = None
    path_finder = PathFinder(config=config)
    return path_finder

def test_edge_case_none(setup_pathfinder):
    with patch('isort.deprecated.finders.os.environ', {'VIRTUAL_ENV': None, 'CONDA_PREFIX': None}):
        module_name = "some_module"
        result = setup_pathfinder.find(module_name)
        assert result is None
