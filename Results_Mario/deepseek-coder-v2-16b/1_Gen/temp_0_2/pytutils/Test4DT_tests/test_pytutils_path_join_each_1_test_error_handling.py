
import os
import pytest
from unittest.mock import patch

def join_each(parent, iterable):
    """
    Generates paths by joining each element of the given iterable with the specified parent directory.
    
    Parameters:
        parent (str): The base directory to which elements from `iterable` will be joined.
        iterable (iterable): An iterable containing strings that will be joined to the `parent`.
    
    Yields:
        str: Paths formed by joining each element of `iterable` with `parent`.
        
    Examples:
        Suppose you have a list of file names ['file1', 'file2'] and you want to join them with '/home/user':
        
        ```python
        for path in join_each('/home/user', ['file1', 'file2']):
            print(path)
        ```
        
        This will output:
        - /home/user/file1
        - /home/user/file2
    
    Note:
        The function assumes that the `parent` path ends with a directory separator (e.g., '/'). If you are unsure, ensure to include it accordingly.
        
    Implementation Details:
        This function iterates over each element in the provided iterable and uses os.path.join to concatenate each element with the parent path. The result is yielded as a new string representing the concatenated path for each element in `iterable`.
    """
    if not isinstance(iterable, (list, tuple)):
        raise ValueError("Iterable must be a list or tuple")
    for p in iterable:
        yield os.path.join(parent, p)

def test_error_handling():
    with pytest.raises(ValueError):
        list(join_each('/home/user', 12345))
