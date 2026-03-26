
import pytest
from pathlib import Path
from isort.api import sort_file
from isort.config import Config, DEFAULT_CONFIG

def test_invalid_input():
    # Test with a non-existent file path
    with pytest.raises(FileNotFoundError):
        sort_file("nonexistent_file.py")
    
    # Test with an unsupported file extension (e.g., txt)
    with open("test_invalid_input.txt", "w") as f:
        f.write("print('Hello, World!')")
        
    with pytest.raises(ValueError):
        sort_file("test_invalid_input.txt")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api_sort_file_1_test_invalid_input
isort/Test4DT_tests/test_isort_api_sort_file_1_test_invalid_input.py:5:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_api_sort_file_1_test_invalid_input.py:5:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""