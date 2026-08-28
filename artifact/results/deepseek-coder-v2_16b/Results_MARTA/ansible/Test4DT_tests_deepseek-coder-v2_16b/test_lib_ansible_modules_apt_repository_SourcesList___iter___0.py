
import pytest
from sources_list import SourcesList
import os
import glob

# Test cases for SourcesList class

def test_valid_case():
    # Create a real instance of SourcesList with minimal args
    sourcelist = SourcesList(module='test_module')
    
    # Assuming the load method is working correctly and we have a default file loaded
    assert len(sourcelist.files) > 0, "Expected at least one source file to be loaded"
    for file, sources in sourcelist.files.items():
        for n, valid, enabled, source, comment in sources:
            assert valid, f"Source should be valid but is not in file {file}"
    
def test_edge_case():
    # Test with None input
    sourcelist = SourcesList(module='test_module')
    assert sourcelist.files == {}, "Expected empty files dictionary for None input"
    
    # Test with empty list
    sourcelist = SourcesList(module='test_module')
    sourcelist.files = {'default': []}  # Simulate loading an empty file
    assert len(sourcelist.files) == 1, "Expected only the default file to be present"
    
def test_error_case():
    with pytest.raises(Exception):
        sourcelist = SourcesList(module='test_module')
        # Force an error by providing invalid input
        sourcelist._parse('invalid line', raise_if_invalid_or_disabled=True)
