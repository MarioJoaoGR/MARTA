
import pytest
from sources_list import SourcesList
import os
import glob

# Test valid case scenario
def test_valid_case():
    sourcelist = SourcesList('my_module')
    assert isinstance(sourcelist, SourcesList)
    assert sourcelist.module == 'my_module'
    assert len(sourcelist.files) > 0

# Test edge case scenario with None input
def test_edge_case_none():
    with pytest.raises(TypeError):
        sourcelist = SourcesList(None)

# Test edge case scenario with empty list input
def test_edge_case_empty_list():
    with pytest.raises(TypeError):
        sourcelist = SourcesList('')

# Test error case scenario raising InvalidSource exception
def test_error_case():
    with pytest.raises(InvalidSource):
        sourcelist = SourcesList('my_module')
        sourcelist._parse("invalid source line")
