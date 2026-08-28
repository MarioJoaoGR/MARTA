
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.apt_repository import UbuntuSourcesList, distro

@pytest.fixture(scope="module")
def valid_instance():
    module = MagicMock()
    module.params = {'codename': 'focal'}
    with patch('ansible.modules.apt_repository.distro.codename', return_value='focal'):
        yield UbuntuSourcesList(module)

@pytest.fixture(scope="module")
def invalid_instance():
    module = MagicMock()
    module.params = {'codename': None}
    with pytest.raises(TypeError):
        yield UbuntuSourcesList(module)



def test_edge_case():
    module = MagicMock()
    module.params = {'codename': None}
    with pytest.raises(AttributeError):
        UbuntuSourcesList(module)