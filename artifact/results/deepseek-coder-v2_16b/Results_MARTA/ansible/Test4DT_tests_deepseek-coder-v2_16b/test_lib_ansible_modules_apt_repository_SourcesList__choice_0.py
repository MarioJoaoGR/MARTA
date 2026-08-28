
import pytest
from sources_list import SourcesList
import os
import glob

@pytest.fixture(scope="module")
def sourcelist():
    return SourcesList('my_module')

# Test Scenario 1: Test standard input for _choice method
def test_valid_input(sourcelist):
    new = 'new_source'
    old = 'old_source'
    result = sourcelist._choice(new, old)
    assert result == new

# Test Scenario 2: Test edge case with None inputs
def test_edge_case(sourcelist):
    new = None
    old = 'default_source'
    result = sourcelist._choice(new, old)
    assert result == old

# Test Scenario 3: Test invalid input handling in _choice method
def test_invalid_input(sourcelist):
    new = 'invalid_source'
    old = None
    with pytest.raises(TypeError):
        sourcelist._choice(new, old)
