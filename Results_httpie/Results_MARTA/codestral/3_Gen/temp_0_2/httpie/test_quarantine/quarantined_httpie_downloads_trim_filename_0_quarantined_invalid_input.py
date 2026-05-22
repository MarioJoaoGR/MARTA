
import os
from unittest.mock import patch

def trim_filename(filename: str, max_len: int) -> str:
    if len(filename) > max_len:
        trim_by = len(filename) - max_len
        name, ext = os.path.splitext(filename)
        if trim_by >= len(name):
            filename = filename[:-trim_by]
        else:
            filename = name[:-trim_by] + ext
    return filename

@pytest.mark.parametrize("filename, max_len, expected", [
    ("longfilenamewithextension.txt", 15, "longfilename.txt"),
    ("shortfile", 20, "shortfile"),
    ("anotherlongfile.with.many.dots.ext", 10, "anoth.ext")
])
def test_trim_filename(filename, max_len, expected):
    with patch('os.path.splitext', return_value=("name", ".ext")):
        assert trim_filename(filename, max_len) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_downloads_trim_filename_0_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_0_test_invalid_input.py:15:1: E0602: Undefined variable 'pytest' (undefined-variable)


"""