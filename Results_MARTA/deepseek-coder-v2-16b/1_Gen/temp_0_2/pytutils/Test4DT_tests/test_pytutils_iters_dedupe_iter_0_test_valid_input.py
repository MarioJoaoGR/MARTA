
import pytest
from pytutils.iters import dedupe_iter

def test_valid_input():
    data = [1, 2, 3, 4, 5, 2, 3]
    expected_output = [1, 2, 3, 4, 5]
    
    result = list(dedupe_iter(data))
    
    assert result == expected_output
