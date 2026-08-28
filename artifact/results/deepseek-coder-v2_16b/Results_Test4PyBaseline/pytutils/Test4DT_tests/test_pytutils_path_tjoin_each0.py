
import pytest
import os
from pytutils.path import join_each

# Test case 1: Joining elements from a list to a directory path
def test_join_each_list():
    file_names = ['file1.txt', 'file2.txt']
    directory_path = 'data'
    expected_output = ['data/file1.txt', 'data/file2.txt']
    assert list(join_each(directory_path, file_names)) == expected_output

# Test case 2: Joining elements from a tuple to a root path
def test_join_each_tuple():
    root_path = '/home/user'
    file_tuples = ('dir1/file3.txt', 'dir2/file4.txt')
    expected_output = ['/home/user/dir1/file3.txt', '/home/user/dir2/file4.txt']
    assert list(join_each(root_path, file_tuples)) == expected_output

# Test case 3: Joining elements from a set to a base path (demonstrating unique paths)
def test_join_each_set():
    base_path = 'shared'
    file_set = {'file5.txt', 'file6.txt'}
    expected_output = ['shared/file5.txt', 'shared/file6.txt']
    assert list(join_each(base_path, file_set)) == expected_output

# Test case 4: Handling an empty iterable
def test_join_each_empty_iterable():
    parent = 'test'
    iterable = []
    expected_output = []
    assert list(join_each(parent, iterable)) == expected_output

# Test case 5: Joining elements with a non-string parent path
def test_join_each_non_string_parent():
    parent = None
    iterable = ['file1.txt']
    with pytest.raises(TypeError):
        list(join_each(parent, iterable))

# Test case 6: Joining elements with a non-iterable input
def test_join_each_non_iterable():
    parent = 'test'
    iterable = None
    with pytest.raises(TypeError):
        list(join_each(parent, iterable))
