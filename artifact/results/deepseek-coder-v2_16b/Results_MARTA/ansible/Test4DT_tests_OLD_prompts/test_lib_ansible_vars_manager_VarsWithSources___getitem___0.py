
import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.manager import VarsWithSources

def test_valid_input():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    assert vars_with_sources['var1'] == 1
    assert vars_with_sources['var2'] == 2

def test_edge_case():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    with patch.dict(vars_with_sources.data, {None: "source"}, clear=True):
        assert vars_with_sources[None] == "source"

def test_invalid_input():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    with pytest.raises(KeyError):
        vars_with_sources['missing_key']
