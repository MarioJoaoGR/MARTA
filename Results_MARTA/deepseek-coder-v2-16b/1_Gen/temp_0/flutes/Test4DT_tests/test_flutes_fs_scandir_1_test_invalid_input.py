
import os
from pathlib import Path
from typing import Iterator, Union
import pytest
from unittest.mock import patch

PathType = Union[Path, str]

def scandir(path: PathType) -> Iterator[PathType]:
    """Lazily iterate over all files and directories under a directory. The returned path is the absolute path of the child file or directory, with the same type as :attr:`path` (:py:class:`pathlib.Path` or :py:class:`str`).

    Parameters:
        path (PathType): Path to the directory. It can be either a `pathlib.Path` object or a string representing the file system path.

    Returns:
        Iterator[PathType]: An iterator over children paths, which will yield absolute paths of files and directories.
    """
    if isinstance(path, Path):
        with os.scandir(path) as it:
            for entry in it:
                yield Path(entry.path)
    else:
        with os.scandir(path) as it:
            for entry in it:
                yield entry.path

@pytest.mark.parametrize("invalid_path", ["/nonexistent/directory", str(Path("/nonexistent/directory"))])
def test_invalid_input(invalid_path):
    with pytest.raises(FileNotFoundError):
        list(scandir(invalid_path))
