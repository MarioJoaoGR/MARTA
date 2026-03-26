
from pathlib import Path
from unittest.mock import patch
import pytest
from isort.api import find_imports_in_paths, Config, DEFAULT_CONFIG
from isort.identify import Import

@pytest.mark.parametrize("paths", [
    ([Path("test_dir")]),
    ([Path("test_dir1"), Path("test_dir2")])
])
def test_find_imports_in_paths(paths):
    with patch('isort.api.files') as mock_files:
        # Mock the files.find method to return a list of file paths
        mock_files.find.return_value = ["file1.py", "file2.py"]
        
        # Call the function under test
        imports = find_imports_in_paths(paths)
        
        # Assert that the function returns an iterator of Import objects
        assert isinstance(imports, Iterator)
        for imp in imports:
            assert isinstance(imp, Import)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api_find_imports_in_paths_0_test_edge_cases
isort/Test4DT_tests/test_isort_api_find_imports_in_paths_0_test_edge_cases.py:21:35: E0602: Undefined variable 'Iterator' (undefined-variable)


"""