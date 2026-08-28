
import pytest
from ansible.modules.apt_repository import UbuntuSourcesList
from unittest.mock import patch, MagicMock


def test_invalid_inputs():
    module = MagicMock()
    with pytest.raises(TypeError):
        UbuntuSourcesList()