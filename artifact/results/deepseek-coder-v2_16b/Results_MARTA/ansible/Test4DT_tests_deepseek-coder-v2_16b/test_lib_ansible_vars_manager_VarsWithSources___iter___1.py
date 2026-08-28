
import pytest
from ansible.vars.manager import VarsWithSources

def test_invalid_input():
    with pytest.raises(TypeError):
        vars_with_sources = VarsWithSources(None)
        vars_with_sources['var1']
