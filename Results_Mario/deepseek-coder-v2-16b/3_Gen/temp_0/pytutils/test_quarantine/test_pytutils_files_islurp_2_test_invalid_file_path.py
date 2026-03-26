
import pytest
from pyutils.files import islurp  # Assuming this module exists and contains the function
import sys

def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        for line in islurp('non_existent_file.txt'):
            print(line)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_files_islurp_2_test_invalid_file_path
pytutils/Test4DT_tests/test_pytutils_files_islurp_2_test_invalid_file_path.py:3:0: E0401: Unable to import 'pyutils.files' (import-error)


"""