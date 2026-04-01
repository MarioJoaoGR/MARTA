
import pytest
from isort.deprecated.finders import KnownPatternFinder
from configparser import ConfigParser

@pytest.fixture
def mock_config():
    config = ConfigParser()
    return config

def test_edge_case_none(mock_config):
    with pytest.raises(TypeError):
        mock_config.set('section1', 'known_patterns', None)
