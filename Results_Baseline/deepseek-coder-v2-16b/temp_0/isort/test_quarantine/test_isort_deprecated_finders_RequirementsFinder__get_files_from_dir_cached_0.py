
import pytest
import os
from pathlib import Path

# Assuming parse_requirements is a function that can be used to set the enabled attribute
def parse_requirements(file_path: Path) -> dict:
    return {"package1": "version1", "package2": "version2"}

class RequirementsFinder:
    exts = ('.txt', '.in')
    enabled = bool(parse_requirements)
    
    @classmethod
    def _get_files_from_dir_cached(cls, path: str) -> list[str]:
        results = []
        for fname in os.listdir(path):
            if "requirements" not in fname:
                continue
            full_path = Path(os.path.join(path, fname))
            if full_path.is_dir():
                for subfile_name in os.listdir(full_path):
                    results.extend(
                        os.path.join(full_path, subfile_name)
                        for ext in cls.exts
                        if subfile_name.endswith(ext)
                    )
                continue
            if full_path.is_file():
                for ext in cls.exts:
                    if fname.endswith(ext):
                        results.append(str(full_path))
                        break
        return results

# Test cases
def test_get_files_from_dir_cached_with_valid_directory():
    finder = RequirementsFinder()
    path = 'test_project'  # Assuming a directory named 'test_project' exists for testing
    os.makedirs(os.path.join(path, 'requirements'))
    open(os.path.join(path, 'requirements', 'file1.txt'), 'w').close()
    open(os.path.join(path, 'requirements', 'file2.in'), 'w').close()
    
    files = finder._get_files_from_dir_cached(path)
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

isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0.py F [100%]

=================================== FAILURES ===================================
_____________ test_get_files_from_dir_cached_with_valid_directory ______________

    def test_get_files_from_dir_cached_with_valid_directory():
        finder = RequirementsFinder()
        path = 'test_project'  # Assuming a directory named 'test_project' exists for testing
>       os.makedirs(os.path.join(path, 'requirements'))

isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = 'test_project/requirements', mode = 511, exist_ok = False

>   ???
E   FileExistsError: [Errno 17] File exists: 'test_project/requirements'

<frozen os>:225: FileExistsError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0.py::test_get_files_from_dir_cached_with_valid_directory
============================== 1 failed in 0.06s ===============================
"""