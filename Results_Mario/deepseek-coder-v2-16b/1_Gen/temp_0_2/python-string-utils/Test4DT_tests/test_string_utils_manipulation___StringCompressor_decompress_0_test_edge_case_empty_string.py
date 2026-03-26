
import pytest
from string_utils.manipulation import __StringCompressor

def test_edge_case_empty_string():
    input_string = ""
    encoding = 'utf-8'
    
    with pytest.raises(ValueError):
        result = __StringCompressor.decompress(input_string, encoding)
