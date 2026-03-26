
import pytest
from flutes.iterator import split_by

def test_valid_case_list():
    iterable = [1, 2, 0, 3, 4, 0, 5]
    separator = 0
    expected_output = [[1, 2], [3, 4], [5]]
    
    result = list(split_by(iterable, empty_segments=False, separator=separator))
    
    assert result == expected_output
