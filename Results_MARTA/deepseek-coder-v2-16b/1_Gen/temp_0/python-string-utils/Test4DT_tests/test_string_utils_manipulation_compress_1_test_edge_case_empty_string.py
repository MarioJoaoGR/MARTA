
import pytest
from string_utils.manipulation import compress, decompress

def test_edge_case_empty_string():
    input_string = ''
    with pytest.raises(ValueError):
        compress(input_string)
