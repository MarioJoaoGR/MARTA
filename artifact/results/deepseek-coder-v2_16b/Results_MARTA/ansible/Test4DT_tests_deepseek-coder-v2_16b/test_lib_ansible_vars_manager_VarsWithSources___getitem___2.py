
import pytest
from ansible.vars.manager import VarsWithSources


def test_invalid_input():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    with pytest.raises(KeyError):
        vars_with_sources['non_existent_key']