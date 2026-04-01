
import os
from pathlib import Path
from typing import Iterator, Union

PathType = Union[str, Path]

def scandir(path: PathType) -> Iterator[PathType]:
    """Lazily iterate over all files and directories under a directory. The returned path is the absolute path of the child file or directory, with the same type as :attr:`path` (:py:class:`pathlib.Path` or :py:class:`str`).

    Parameters:
        path (PathType): Path to the directory. It can be either a string representing a file system path or an instance of `pathlib.Path`.

    Returns:
        Iterator[PathType]: An iterator over children paths, which will be instances of `pathlib.Path` if the input is a `pathlib.Path` object, otherwise they will be strings.

    Examples:
        To iterate over all files and directories in the current working directory:
        
        ```python
        from pathlib import Path
        
        for entry in scandir(Path.cwd()):
            print(entry)
        ```
        
        To iterate over all files and directories in a specific directory:
        
        ```python
        from pathlib import Path
        
        for entry in scandir(Path('/some/directory')):
            print(entry)
        ```
    
    This function is designed to provide a lazy iterator that efficiently scans through all files and directories located under the specified directory. It supports both `pathlib.Path` objects and string paths, making it versatile for different usage scenarios in a Python environment. The implementation ensures compatibility with both path types while maintaining performance by using `os.scandir` for efficient directory scanning.
    """
    if isinstance(path, Path):
        with os.scandir(path) as it:
            for entry in it:
                yield Path(entry.path)
    else:
        with os.scandir(path) as it:
            for entry in it:
                yield entry.path

# Test case to ensure TypeError is raised when input is None
def test_none_input():
    with pytest.raises(TypeError):
        scandir(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_scandir_0_test_none_input
flutes/Test4DT_tests/test_flutes_fs_scandir_0_test_none_input.py:49:9: E0602: Undefined variable 'pytest' (undefined-variable)


"""