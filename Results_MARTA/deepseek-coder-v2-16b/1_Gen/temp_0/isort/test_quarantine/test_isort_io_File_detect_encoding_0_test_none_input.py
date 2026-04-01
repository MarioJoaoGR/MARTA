
import pytest
from pathlib import Path
from io import TextIOBase
from tokenize import detect_encoding
from isort.io import UnsupportedEncoding

def test_none_input():
    with pytest.raises(UnsupportedEncoding):
        File.detect_encoding("non_existent_file", lambda: b"line")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_io_File_detect_encoding_0_test_none_input
isort/Test4DT_tests/test_isort_io_File_detect_encoding_0_test_none_input.py:10:8: E0602: Undefined variable 'File' (undefined-variable)


"""