
import pytest
from sources_list import SourcesList

# Test Scenario 1: Adding a valid source line with comment and specified file name
def test_valid_input():
    sourcelist = SourcesList(module='apt_module')
    sourcelist.add_source('deb http://example.com/ubuntu focal main', comment='# This is an example source', file='sources.list')
    
    assert 'deb http://example.com/ubuntu focal main' in sourcelist.files['sources.list']
    assert '# This is an example source' == sourcelist.files['sources.list'][0][2]

# Test Scenario 2: Adding a source line with None input
def test_edge_case():
    sourcelist = SourcesList(module='apt_module')
    with pytest.raises(Exception):
        sourcelist.add_source(None, comment=None, file=None)

# Test Scenario 3: Adding a source line with invalid format
def test_invalid_input():
    sourcelist = SourcesList(module='apt_module')
    with pytest.raises(Exception):
        sourcelist.add_source('invalid_format', comment='Invalid comment', file='sources.list')
