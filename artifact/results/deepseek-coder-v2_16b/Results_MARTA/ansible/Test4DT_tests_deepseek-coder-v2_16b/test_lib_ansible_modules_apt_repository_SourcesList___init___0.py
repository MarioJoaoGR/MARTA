
import pytest
from sources_list import SourcesList
import os
import glob

# Test scenarios
def test_valid_case():
    sourcelist = SourcesList(module='my_module')
    assert sourcelist.module == 'my_module'
    assert isinstance(sourcelist.files, dict)
    assert isinstance(sourcelist.new_repos, set)
    assert os.path.isfile(sourcelist.default_file)

def test_edge_case():
    sourcelist = SourcesList(module='my_module')
    with pytest.raises(TypeError):
        sourcelist._parse(None)
    with pytest.raises(TypeError):
        sourcelist._apt_cfg_file(None)
    with pytest.raises(TypeError):
        sourcelist._apt_cfg_dir(None)

def test_error_case():
    with pytest.raises(TypeError):
        SourcesList(module=None)
