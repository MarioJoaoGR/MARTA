
import pytest
from youtube_dl.aes import rotate

# Test cases for the rotate function

def test_rotate_basic():
    assert rotate([1, 2, 3, 4]) == [2, 3, 4, 1]
    assert rotate([65, 66, 67]) == [66, 67, 65]

def test_rotate_empty():
    with pytest.raises(IndexError):
        rotate([])

def test_rotate_single_element():
    assert rotate([1]) == [1]

def test_rotate_large_list():
    assert rotate([10, 20, 30, 40, 50]) == [20, 30, 40, 50, 10]
