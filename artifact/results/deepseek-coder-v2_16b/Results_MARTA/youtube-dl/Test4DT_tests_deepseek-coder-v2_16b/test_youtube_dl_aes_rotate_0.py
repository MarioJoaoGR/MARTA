
import pytest
from youtube_dl.aes import rotate


def test_rotate_single_element():
    assert rotate([1]) == [1]

def test_rotate_multiple_elements():
    assert rotate([1, 2, 3]) == [2, 3, 1]

def test_rotate_string_list():
    assert rotate(['a', 'b', 'c']) == ['b', 'c', 'a']