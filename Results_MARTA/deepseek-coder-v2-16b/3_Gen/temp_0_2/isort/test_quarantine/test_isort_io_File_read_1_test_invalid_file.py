
import pytest
from pathlib import Path
from unittest.mock import patch

@pytest.mark.parametrize("filename", ["nonexistent_file.txt"])
def test_invalid_file(filename):
    with pytest.raises(FileNotFoundError):
        list(File.read(filename))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_io_File_read_1_test_invalid_file
isort/Test4DT_tests/test_isort_io_File_read_1_test_invalid_file.py:9:13: E0602: Undefined variable 'File' (undefined-variable)


"""