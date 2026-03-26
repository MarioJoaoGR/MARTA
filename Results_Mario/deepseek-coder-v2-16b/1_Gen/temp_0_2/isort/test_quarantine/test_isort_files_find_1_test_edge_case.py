
import os
from pathlib import Path
from typing import Iterable, Iterator
from isort.config import Config  # Corrected import from isort module

def find(
    paths: Iterable[str], config: Config, skipped: list[str], broken: list[str]
) -> Iterator[str]:
    """Fines and provides an iterator for all Python source files defined in the given paths.

    This function searches through the provided file or directory paths to find and yield all Python source files. It respects configuration settings, including whether to follow symlinks and which files to skip based on the config object's settings.

    Parameters:
        - `paths` (Iterable[str]): An iterable of file or directory paths from which to search for Python source files.
        - `config` (Config): A Config object that contains configuration settings including whether to follow symlinks and a method to check if a file should be skipped.
        - `skipped` (list[str]): A list to which the paths of directories or files that are skipped due to config settings will be appended.
        - `broken` (list[str]): A list to which the paths of non-existent file or directory paths will be appended.

    Returns:
        An iterator over strings, where each string is a path to a Python source file found in the provided paths.
    """
    visited_dirs: set[Path] = set()

    for path in paths:
        if os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(
                path, topdown=True, followlinks=config.follow_links
            ):
                base_path = Path(dirpath)
                for dirname in list(dirnames):
                    full_path = base_path / dirname
                    resolved_path = full_path.resolve()
                    if config.is_skipped(full_path):
                        skipped.append(str(full_path))
                        dirnames.remove(dirname)
                    else:
                        if resolved_path in visited_dirs:  # pragma: no cover
                            dirnames.remove(dirname)
                    visited_dirs.add(resolved_path)

                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    if config.is_supported_filetype(filepath):
                        if config.is_skipped(Path(os.path.abspath(filepath))):
                            skipped.append(os.path.abspath(filepath))
                        else:
                            yield filepath
        elif not os.path.exists(path):
            broken.append(path)
        else:
            yield path

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_files_find_1_test_edge_case
isort/Test4DT_tests/test_isort_files_find_1_test_edge_case.py:5:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_files_find_1_test_edge_case.py:5:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""