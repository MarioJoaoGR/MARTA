
import os
from unittest.mock import patch
import pytest

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
    (None, 20, None),
    ("longfilenamewithextension.txt", 15, "longfilename.txt"),
    ("shortfile", 20, "shortfile"),
    ("anotherlongfile.with.many.dots.ext", 10, "anoth.ext")
])
def test_trim_filename(filename, max_len, expected):
    with patch('os.path.splitext', return_value=('', '.txt')):
        assert trim_filename(filename, max_len) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_2_test_edge_case_none.py F [ 25%]
F.F                                                                      [100%]

=================================== FAILURES ===================================
_______________________ test_trim_filename[None-20-None] _______________________

filename = None, max_len = 20, expected = None

    @pytest.mark.parametrize("filename, max_len, expected", [
        (None, 20, None),
        ("longfilenamewithextension.txt", 15, "longfilename.txt"),
        ("shortfile", 20, "shortfile"),
        ("anotherlongfile.with.many.dots.ext", 10, "anoth.ext")
    ])
    def test_trim_filename(filename, max_len, expected):
        with patch('os.path.splitext', return_value=('', '.txt')):
>           assert trim_filename(filename, max_len) == expected

httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_2_test_edge_case_none.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = None, max_len = 20

    def trim_filename(filename: str, max_len: int) -> str:
>       if len(filename) > max_len:
E       TypeError: object of type 'NoneType' has no len()

httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_2_test_edge_case_none.py:7: TypeError
____ test_trim_filename[longfilenamewithextension.txt-15-longfilename.txt] _____

filename = 'longfilenamewithextension.txt', max_len = 15
expected = 'longfilename.txt'

    @pytest.mark.parametrize("filename, max_len, expected", [
        (None, 20, None),
        ("longfilenamewithextension.txt", 15, "longfilename.txt"),
        ("shortfile", 20, "shortfile"),
        ("anotherlongfile.with.many.dots.ext", 10, "anoth.ext")
    ])
    def test_trim_filename(filename, max_len, expected):
        with patch('os.path.splitext', return_value=('', '.txt')):
>           assert trim_filename(filename, max_len) == expected
E           AssertionError: assert 'longfilenamewit' == 'longfilename.txt'
E             
E             - longfilename.txt
E             ?             ^ --
E             + longfilenamewit
E             ?             ^^

httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_2_test_edge_case_none.py:24: AssertionError
_____ test_trim_filename[anotherlongfile.with.many.dots.ext-10-anoth.ext] ______

filename = 'anotherlongfile.with.many.dots.ext', max_len = 10
expected = 'anoth.ext'

    @pytest.mark.parametrize("filename, max_len, expected", [
        (None, 20, None),
        ("longfilenamewithextension.txt", 15, "longfilename.txt"),
        ("shortfile", 20, "shortfile"),
        ("anotherlongfile.with.many.dots.ext", 10, "anoth.ext")
    ])
    def test_trim_filename(filename, max_len, expected):
        with patch('os.path.splitext', return_value=('', '.txt')):
>           assert trim_filename(filename, max_len) == expected
E           AssertionError: assert 'anotherlon' == 'anoth.ext'
E             
E             - anoth.ext
E             + anotherlon

httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_2_test_edge_case_none.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_2_test_edge_case_none.py::test_trim_filename[None-20-None]
FAILED httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_2_test_edge_case_none.py::test_trim_filename[longfilenamewithextension.txt-15-longfilename.txt]
FAILED httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_2_test_edge_case_none.py::test_trim_filename[anotherlongfile.with.many.dots.ext-10-anoth.ext]
========================= 3 failed, 1 passed in 0.15s ==========================
"""