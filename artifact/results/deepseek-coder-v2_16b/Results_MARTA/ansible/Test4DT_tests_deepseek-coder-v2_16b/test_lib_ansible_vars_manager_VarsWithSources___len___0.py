
import pytest
from ansible.vars.manager import VarsWithSources

def test_invalid_inputs():
    with pytest.raises(TypeError):
        VarsWithSources(None)
