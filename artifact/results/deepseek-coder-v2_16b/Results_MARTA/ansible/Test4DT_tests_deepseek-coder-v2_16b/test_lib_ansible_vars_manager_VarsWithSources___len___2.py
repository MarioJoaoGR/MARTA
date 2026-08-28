
import pytest
from ansible.vars.manager import VarsWithSources

def test_VarsWithSources_initialization():
    vs = VarsWithSources({'var1': 1, 'var2': 2})
    assert len(vs) == 2


