
import os
from pathlib import Path
from typing import Iterator, Union

PathType = Union[Path, str]

def scandir(path: PathType) -> Iterator[PathType]:
    r"""Lazily iterate over all files and directories under a directory. The returned path is the absolute path of the
    child file or directory, with the same type as :attr:`path` (:py:class:`pathlib.Path` or :py:class:`str`).

    :param path: Path to the directory.
    :return: An iterator over children paths.
    """
    if isinstance(path, Path):
        with os.scandir(path) as it:
            for entry in it:
                yield Path(entry.path)
    else:
        with os.scandir(path) as it:
            for entry in it:
                yield entry.path

# Test case for handling None input
def test_none_input():
    from unittest.mock import patch
    
    # Mock the behavior of scandir to raise an exception when path is None
    with patch('os.scandir', side_effect=ValueError("Invalid path")):
        try:
            list(scandir(None))  # This should raise a ValueError
        except ValueError as e:
            assert str(e) == "Invalid path"
        else:
            assert False, "Expected a ValueError but no exception was raised"
