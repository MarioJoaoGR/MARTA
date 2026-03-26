# Module: pytutils.path
import pytest
import os
from pytutils.path import join_each

# Test case 1: Basic usage with `os.path.join`
def test_basic_usage():
    parent = '/home/user'
    iterable = ['file1', 'file2']
    expected_output = ['/home/user/file1', '/home/user/file2']
    assert list(join_each(parent, iterable)) == expected_output

# Test case 2: Using the function with a different parent path
def test_different_parent_path():
    parent = '/data'
    iterable = ['logs', 'reports']
    expected_output = ['/data/logs', '/data/reports']
    assert list(join_each(parent, iterable)) == expected_output

# Test case 3: Handling an empty iterable
def test_empty_iterable():
    parent = '/empty'
    iterable = []
    expected_output = []
    assert list(join_each(parent, iterable)) == expected_output

# Test case 4: Using the function with a single element in the iterable
def test_single_element_in_iterable():
    parent = '/single'
    iterable = ['file']
    expected_output = ['/single/file']
    assert list(join_each(parent, iterable)) == expected_output

# Test case 5: Handling non-string elements in the iterable (should raise a TypeError)
def test_non_string_elements():
    parent = '/invalid'
    iterable = [123, None]  # Including non-string types to check for type errors
    with pytest.raises(TypeError):
        list(join_each(parent, iterable))
