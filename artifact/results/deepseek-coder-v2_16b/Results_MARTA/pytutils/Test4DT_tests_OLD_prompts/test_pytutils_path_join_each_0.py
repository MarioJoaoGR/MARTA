
import pytest
from pytutils.path import join_each
import os

def test_join_each_basic():
    parent = "/root/directory"
    iterable = ["file1.txt", "file2.txt", "file3.txt"]
    
    expected_output = [
        "/root/directory/file1.txt",
        "/root/directory/file2.txt",
        "/root/directory/file3.txt"
    ]
    
    result = list(join_each(parent, iterable))
    assert result == expected_output

def test_join_each_with_different_iterable():
    parent = "/root/directory"
    iterable = ["dir1", "file1.txt", "dir2"]
    
    expected_output = [
        "/root/directory/dir1",
        "/root/directory/file1.txt",
        "/root/directory/dir2"
    ]
    
    result = list(join_each(parent, iterable))
    assert result == expected_output

def test_join_each_with_empty_iterable():
    parent = "/root/directory"
    iterable = []
    
    expected_output = []
    
    result = list(join_each(parent, iterable))
    assert result == expected_output

def test_join_each_with_non_string_elements():
    parent = "/root/directory"
    iterable = ["file1.txt", 123, "file2.txt"]
    
    with pytest.raises(TypeError):
        list(join_each(parent, iterable))
