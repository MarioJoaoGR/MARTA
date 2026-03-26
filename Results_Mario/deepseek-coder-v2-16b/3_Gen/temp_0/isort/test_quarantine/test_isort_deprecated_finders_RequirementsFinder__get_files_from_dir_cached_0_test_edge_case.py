
import os
from unittest.mock import patch
import pytest
from isort.deprecated.finders import RequirementsFinder

class RequirementsFinder:
    exts = '.txt', '.in'
    enabled = bool(parse_requirements)
    
    def _get_files_from_dir_cached(cls, path: str) -> list[str]:
        results: list[str] = []
        
        for fname in os.listdir(path):
            if "requirements" not in fname:
                continue
            full_path = os.path.join(path, fname)
            
            # *requirements*/*.{txt,in}
            if os.path.isdir(full_path):
                for subfile_name in os.listdir(full_path):
                    results.extend(
                        os.path.join(full_path, subfile_name)
                        for ext in cls.exts
                        if subfile_name.endswith(ext)
                    )
                continue
            
            # *requirements*.{txt,in}
            if os.path.isfile(full_path):
                for ext in cls.exts:
                    if fname.endswith(ext):
                        results.append(full_path)
                        break
        
        return results

@pytest.mark.parametrize("test_input, expected", [
    ('mock_dir', ['mock_dir/requirements/file1.txt', 'mock_dir/requirements/file2.in'])
])
def test_get_files_from_dir_cached(test_input, expected):
    with patch('os.listdir', return_value=['requirements']), \
         patch('os.path.isdir', side_effect=[True, False]), \
         patch('os.path.isfile', side_effect=[False, True]):
        finder = RequirementsFinder()
        assert finder._get_files_from_dir_cached(test_input) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_edge_case
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_edge_case.py:7:0: E0102: class already defined line 5 (function-redefined)
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_edge_case.py:9:19: E0602: Undefined variable 'parse_requirements' (undefined-variable)
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_files_from_dir_cached_0_test_edge_case.py:11:4: E0213: Method '_get_files_from_dir_cached' should have "self" as first argument (no-self-argument)


"""