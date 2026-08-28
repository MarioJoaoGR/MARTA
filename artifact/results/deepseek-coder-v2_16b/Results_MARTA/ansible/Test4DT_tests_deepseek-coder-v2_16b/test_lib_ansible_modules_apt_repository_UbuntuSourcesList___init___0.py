
import pytest
from ansible.modules.apt_repository import UbuntuSourcesList
from unittest.mock import patch, MagicMock
import distro


def test_initialization_without_codename():
    module = MagicMock()
    module.params = {'codename': None}
    with patch('distro.codename', return_value='bionic'):
        with pytest.raises(AttributeError):
            sources_list = UbuntuSourcesList(module)