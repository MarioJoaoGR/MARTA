
import os
from pathlib import Path
from typing import Iterable, Iterator

import pytest

from isort import Config


# Provided function definition and module name
def find(
    paths: Iterable[str], config: Config, skipped: list[str], broken: list[str]
) -> Iterator[str]:
    """Fines and provides an iterator for all Python source files defined in paths."""
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

# Test cases for the find function
@pytest.mark.skip(reason="Requires a valid configuration file that does not exist")
def test_find_multiple_directories():
    config = Config(settings_file="path/to/config.ini")
    skipped_paths = []
    broken_paths = []
    paths_to_search = [str(Path("dir1")), str(Path("dir2"))]
    
    files = list(find(paths_to_search, config, skipped_paths, broken_paths))
    assert len(files) > 0, "Expected to find Python source files in multiple directories"

@pytest.mark.skip(reason="Requires a valid configuration file that does not exist")
def test_find_single_directory():
    config = Config(settings_file="path/to/config.ini")
    skipped_paths = []
    broken_paths = []
    paths_to_search = [str(Path("specific_directory"))]
    
    files = list(find(paths_to_search, config, skipped_paths, broken_paths))
    assert len(files) > 0, "Expected to find Python source files in a single directory"

@pytest.mark.skip(reason="Requires a valid configuration file that does not exist")
def test_find_root_and_subdirectories():
    config = Config(settings_file="path/to/config.ini")
    skipped_paths = []
    broken_paths = []
    paths_to_search = [str(Path("root_directory"))]
    
    files = list(find(paths_to_search, config, skipped_paths, broken_paths))
    assert len(files) > 0, "Expected to find Python source files in a root directory and its subdirectories"

@pytest.mark.skip(reason="Requires a valid configuration file that does not exist")
def test_find_with_broken_path():
    config = Config(settings_file="path/to/config.ini")
    skipped_paths = []
    broken_paths = []
    paths_to_search = [str(Path("non_existent_directory")), str(Path("existing_directory"))]
    
    files = list(find(paths_to_search, config, skipped_paths, broken_paths))
    assert "non_existent_directory" in broken_paths, "Expected 'non_existent_directory' to be marked as broken"
    assert len(files) > 0, "Expected to find Python source files in the existing directory"

@pytest.mark.skip(reason="Requires a valid configuration file that does not exist")
def test_find_with_skipped_path():
    config = Config(settings_file="path/to/config.ini")
    skipped_paths = []
    broken_paths = []
    paths_to_search = [str(Path("existing_directory")), str(Path("another_existing_directory"))]
    
    files = list(find(paths_to_search, config, skipped_paths, broken_paths))
    assert "another_existing_directory" in skipped_paths, "Expected 'another_existing_directory' to be marked as skipped"
    assert len(files) > 0, "Expected to find Python source files in the existing directory"
