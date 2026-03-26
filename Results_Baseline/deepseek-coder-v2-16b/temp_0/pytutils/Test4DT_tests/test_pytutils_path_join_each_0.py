
import pytest
import os
from pytutils.path import join_each

# Test cases for join_each function

def test_join_each_basic():
    result = list(join_each('parent_dir', ['child1', 'child2']))
    assert result == ['parent_dir/child1', 'parent_dir/child2']

def test_join_each_generator():
    paths = []
    for path in join_each('base_path', ['folder1', 'file1.txt']):
        paths.append(path)
    assert paths == ['base_path/folder1', 'base_path/file1.txt']

def test_join_each_os_module():
    import os
    result = list(join_each('parent_dir', ['child1', 'child2']))
    assert result == ['parent_dir/child1', 'parent_dir/child2']

# Edge cases to consider:
def test_join_each_empty_iterable():
    result = list(join_each('parent_dir', []))
    assert result == []

def test_join_each_none_parent():
    with pytest.raises(TypeError):
        list(join_each(None, ['child1', 'child2']))

def test_join_each_none_iterable():
    with pytest.raises(TypeError):
        list(join_each('parent_dir', None))

# Additional tests for robustness and error handling:
def test_join_each_non_string_elements():
    with pytest.raises(TypeError):
        list(join_each('parent_dir', [123, 'child2']))  # Non-string elements in iterable
