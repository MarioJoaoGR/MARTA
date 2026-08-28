
import pytest
from os import fspath

class PathLike:
    """
    Abstract base class for implementing the file system path protocol.
    """

    def __fspath__(self) -> str:
        """
        Intended to be overridden by subclasses to provide a string that represents the file system path.

        Returns:
            str: The file system path as a string when implemented in a subclass.

        Raises:
            NotImplementedError: If called on an instance of the base class without being overridden.
        """
        raise NotImplementedError

class MyPath(PathLike):
    def __init__(self, path):
        self._path = path

    def __fspath__(self) -> str:
        if not isinstance(self._path, str) or not self._path:
            raise ValueError('Invalid path')
        return self._path

def test_valid_case():
    my_path = MyPath('/valid/path')
    assert fspath(my_path) == '/valid/path'

def test_edge_case():
    my_path_none = MyPath(None)
    with pytest.raises(ValueError):
        fspath(my_path_none)

    my_path_empty = MyPath('')
    with pytest.raises(ValueError):
        fspath(my_path_empty)

def test_invalid_case():
    my_path_invalid = MyPath(123)
    with pytest.raises(ValueError):
        fspath(my_path_invalid)
