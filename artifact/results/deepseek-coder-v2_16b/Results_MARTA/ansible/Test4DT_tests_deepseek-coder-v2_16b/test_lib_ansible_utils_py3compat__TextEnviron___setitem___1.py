
import pytest
from ansible.utils import py3compat

@pytest.fixture(scope="module")
def text_environ():
    return py3compat._TextEnviron()

def test_invalid_inputs(text_environ):
    with pytest.raises(TypeError):
        text_environ['INVALID_KEY'] = b'INVALID_VALUE'
