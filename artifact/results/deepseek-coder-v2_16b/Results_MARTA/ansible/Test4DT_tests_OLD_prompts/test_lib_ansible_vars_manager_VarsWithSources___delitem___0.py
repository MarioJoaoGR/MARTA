
import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.manager import VarsWithSources

# Test Scenario 1: test_valid_input
def test_valid_input():
    vs = VarsWithSources({'var1': 1, 'var2': 2})
    assert vs['var1'] == 1
    assert vs['var2'] == 2

# Test Scenario 2: test_edge_case
def test_edge_case():
    vs = VarsWithSources()
    with pytest.raises(KeyError):
        vs['non_existent_key']

# Test Scenario 3: test_invalid_input
def test_invalid_input():
    vs = VarsWithSources({'var1': 1})
    with pytest.raises(KeyError):
        del vs['non_existent_key']
