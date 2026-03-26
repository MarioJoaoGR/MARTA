
import os
from pathlib import Path
from typing import Iterable, Iterator
from unittest.mock import MagicMock
import pytest

# Assuming Config class is defined elsewhere in the codebase
class Config:
    def __init__(self):
        self.follow_links = True
    
    def is_skipped(self, path: Path) -> bool:
        return False
    
    def is_supported_filetype(self, filepath: str) -> bool:
        return filepath.endswith('.py')

def find(
    paths: Iterable[str], config: Config, skipped: list[str], broken: list[str]
) -> Iterator[str]:
    """Fines and provides an iterator for all Python source files defined in the given paths."""
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

# Mock setup for Config class
@pytest.fixture
def mock_config():
    config = Config()
    config.follow_links = True
    config.is_skipped = MagicMock(return_value=False)
    config.is_supported_filetype = MagicMock(side_effect=lambda x: x.endswith('.py'))
    return config

def test_valid_case():
    paths = ["test_dir"]
    skipped_files = []
    broken_paths = []
    config = mock_config()
    
    # Create a valid directory structure for testing
    os.makedirs("test_dir/subdir1")
    open("test_dir/subdir1/file1.py", "w").close()
    open("test_dir/subdir1/file2.txt", "w").close()  # This should be skipped
    
    python_files = list(find(paths, config, skipped_files, broken_paths))
    
    assert len(python_files) == 1
    assert python_files[0] == "test_dir/subdir1/file1.py"
    assert not os.path.exists("test_dir/subdir1/file2.txt")
    assert "test_dir/subdir1/file2.txt" in skipped_files
    
    # Clean up the test directory
    import shutil
    shutil.rmtree("test_dir")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_files_find_0_test_valid_case.py F         [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________
Fixture "mock_config" called directly. Fixtures are not meant to be called directly,
but are created automatically when test functions request them as parameters.
See https://docs.pytest.org/en/stable/explanation/fixtures.html for more information about fixtures, and
https://docs.pytest.org/en/stable/deprecations.html#calling-fixtures-directly about how to update your code.
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_files_find_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.05s ===============================
"""