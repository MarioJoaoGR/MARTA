
import pytest
from ansible.galaxy.api import GalaxyAPI


def test_invalid_inputs():
    # Test initialization with invalid inputs to ensure it raises the expected TypeError
    with pytest.raises(TypeError) as excinfo:
        api = GalaxyAPI('invalidName', 'https://invalid-server.com')
    assert str(excinfo.value) == "GalaxyAPI.__init__() missing 1 required positional argument: 'url'"