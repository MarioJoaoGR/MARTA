
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.apt_repository import UbuntuSourcesList




def test_invalid_param():
    module = MagicMock()
    module.params = {'invalid_param': 'focal'}

    with patch('distro.codename', return_value='focal'):
        with pytest.raises(KeyError):
            UbuntuSourcesList(module)