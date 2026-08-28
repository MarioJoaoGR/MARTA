
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.apt_repository import SourcesList

@pytest.fixture(autouse=True)
def mock_apt_pkg():
    with patch('ansible.modules.apt_repository.apt_pkg'):
        yield

@pytest.fixture
def sourcelist():
    return SourcesList('my_module')

def test_sourceslist_init_with_default_sources(sourcelist):
    assert sourcelist.default_file is not None
    assert len(sourcelist.files) > 0 or sourcelist.default_file == 'Dir::Etc::sourcelist'


