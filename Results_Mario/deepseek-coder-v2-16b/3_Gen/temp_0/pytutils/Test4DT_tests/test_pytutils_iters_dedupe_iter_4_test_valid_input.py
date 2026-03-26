
import pytest
from pytutils.iters import dedupe_iter

def test_valid_input():
    # Test case 1: List of integers without duplicates
    assert list(dedupe_iter([1, 2, 3])) == [1, 2, 3]
    
    # Test case 2: List of integers with duplicates
    assert list(dedupe_iter([1, 2, 3, 2, 1])) == [1, 2, 3]
    
    # Test case 3: List of strings without duplicates
    assert list(dedupe_iter(['a', 'b', 'c'])) == ['a', 'b', 'c']
    
    # Test case 4: List of strings with duplicates
    assert list(dedupe_iter(['a', 'b', 'c', 'b', 'a'])) == ['a', 'b', 'c']
    
    # Test case 5: List of mixed types without duplicates
    assert list(dedupe_iter([1, 'a', 2, 'b', 3])) == [1, 'a', 2, 'b', 3]
    
    # Test case 6: List of mixed types with duplicates
    assert list(dedupe_iter([1, 'a', 2, 'b', 1, 'a'])) == [1, 'a', 2, 'b']
