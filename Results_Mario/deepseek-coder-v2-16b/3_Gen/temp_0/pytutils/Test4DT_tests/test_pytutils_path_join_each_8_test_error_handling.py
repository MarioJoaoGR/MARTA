
import os
import pytest
from unittest.mock import patch

def join_each(parent, iterable):
    """
    Join each element of an iterable to a parent path using the `os.path.join` function.

    Parameters:
        parent (str): The base directory or path to which elements from the iterable will be joined.
        iterable (iterable): An iterable containing strings that are to be joined with the parent path.

    Yields:
        str: A new string where each element of the iterable is joined to the parent path using `os.path.join`.

    Examples:
        >>> list(join_each('parent_dir', ['child1', 'child2']))
        ['parent_dir/child1', 'parent_dir/child2']

        >>> for path in join_each('base_path', ['folder1', 'file1.txt']):
        ...     print(path)
        base_path/folder1
        base_path/file1.txt

    This function is useful for constructing file paths from a common parent directory, which can be particularly helpful when dealing with hierarchical data structures in operating systems where path concatenation might be required.
    """
    for p in iterable:
        yield os.path.join(parent, p)

def test_error_handling():
    with pytest.raises(TypeError):
        list(join_each('parent_dir', ['child1', 123]))
