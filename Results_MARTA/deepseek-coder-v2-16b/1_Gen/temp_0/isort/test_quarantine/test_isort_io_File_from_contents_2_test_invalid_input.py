
import pytest
from io import StringIO, BytesIO
from pathlib import Path
from unittest.mock import patch
from isort.io import File

def test_invalid_input():
    with pytest.raises(UnsupportedEncoding):
        File.from_contents("example content", "example_file.txt")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_io_File_from_contents_2_test_invalid_input
isort/Test4DT_tests/test_isort_io_File_from_contents_2_test_invalid_input.py:9:23: E0602: Undefined variable 'UnsupportedEncoding' (undefined-variable)


"""