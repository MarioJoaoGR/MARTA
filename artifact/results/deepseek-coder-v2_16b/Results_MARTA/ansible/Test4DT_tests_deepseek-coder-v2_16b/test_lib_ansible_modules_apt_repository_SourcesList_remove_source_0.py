
import pytest
from sources_list import SourcesList

# Test Scenario 1: Valid Input
def test_valid_input():
    sourcelist = SourcesList(module='apt_module')
    sourcelist.files['sources.list'] = ['deb http://example.com/ubuntu focal main', 'deb http://example.org/debian stretch main']
    sourcelist.remove_source('deb http://example.com/ubuntu focal main')
    assert len(sourcelist.files['sources.list']) == 1
    assert 'deb http://example.com/ubuntu focal main' not in sourcelist.files['sources.list']

# Test Scenario 2: Edge Case - None Input
def test_edge_case():
    sourcelist = SourcesList(module='apt_module')
    sourcelist.files['sources.list'] = ['deb http://example.com/ubuntu focal main', 'deb http://example.org/debian stretch main']
    source_to_remove = None
    with pytest.raises(Exception) as e:
        sourcelist.remove_source(source_to_remove)
    assert str(e.value) == 'InvalidSource: Invalid or disabled source'

# Test Scenario 3: Invalid Input
def test_invalid_input():
    sourcelist = SourcesList(module='apt_module')
    sourcelist.files['sources.list'] = ['deb http://example.com/ubuntu focal main', 'deb http://example.org/debian stretch main']
    invalid_source_line = 'invalid source line'
    with pytest.raises(Exception) as e:
        sourcelist.remove_source(invalid_source_line)
    assert str(e.value) == 'InvalidSource: Invalid or disabled source'
