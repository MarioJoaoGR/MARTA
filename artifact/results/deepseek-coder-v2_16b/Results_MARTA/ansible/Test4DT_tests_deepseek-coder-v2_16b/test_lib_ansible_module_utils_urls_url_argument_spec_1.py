
import pytest
from ansible.module_utils.urls import url_argument_spec

def test_invalid_inputs():
    with pytest.raises(TypeError):
        url_argument_spec({'url': None})
