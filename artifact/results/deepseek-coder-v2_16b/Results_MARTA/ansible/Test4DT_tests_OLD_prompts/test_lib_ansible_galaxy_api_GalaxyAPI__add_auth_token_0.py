
import pytest
from unittest.mock import patch
from ansible.galaxy.api import GalaxyAPI
from ansible.errors import AnsibleError


def test_invalid_inputs():
    with pytest.raises(TypeError):
        GalaxyAPI()