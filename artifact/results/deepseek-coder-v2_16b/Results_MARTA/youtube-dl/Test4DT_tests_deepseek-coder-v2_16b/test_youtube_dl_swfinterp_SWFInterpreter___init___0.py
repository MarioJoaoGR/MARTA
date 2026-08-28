
import pytest
from youtube_dl.swfinterp import SWFInterpreter
import io

# Test for valid SWF file

# Test for non-SWF file
def test_non_swf_file():
    # Create a mock non-SWF content (this is just an example, replace with actual non-SWF data)
    non_swf_content = b'mock non-SWF content'
    
    # Open and read the non-SWF file content
    with pytest.raises(Exception):  # Expecting a specific exception for non-SWF files
        SWFInterpreter(non_swf_content)