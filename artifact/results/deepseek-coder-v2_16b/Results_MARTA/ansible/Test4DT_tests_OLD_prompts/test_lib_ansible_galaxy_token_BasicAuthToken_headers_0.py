
import pytest
from ansible.galaxy.token import BasicAuthToken

def test_invalid_inputs():
    with pytest.raises(TypeError):
        BasicAuthToken()
