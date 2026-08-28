
import pytest
from sources_list import SourcesList
import os
import glob

# Test valid input scenario
def test_valid_input():
    sourcelist = SourcesList(module='my_module')
    assert isinstance(sourcelist.files, dict)
    assert sourcelist.module == 'my_module'
    assert os.path.isfile(sourcelist.default_file)

# Test edge case scenario with None input
def test_edge_case():
    sourcelist = SourcesList(module=None)
    assert sourcelist.module is None
    assert not sourcelist.files
    assert not sourcelist.new_repos

# Test invalid input scenario
def test_invalid_input():
    with pytest.raises(TypeError):
        sourcelist = SourcesList('invalid_type')
