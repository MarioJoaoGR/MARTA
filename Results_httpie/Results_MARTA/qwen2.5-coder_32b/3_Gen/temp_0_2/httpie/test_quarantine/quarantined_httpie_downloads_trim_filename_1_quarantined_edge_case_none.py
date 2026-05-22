
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
@patch('os.path.splitext')
def test_trim_filename(mock_splitext, filename, max_len, expected):
    if filename is None:
        with pytest.raises(TypeError):
            trim_filename(filename, max_len)
    else:
        mock_splitext.return_value = ("name", "ext")
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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_trim_filename_1_test_edge_case_none.py . [ 25%]
F.F                                                                      [100%]

=================================== FAILURES ===================================
____ test_trim_filename[longfilenamewithextension.txt-15-longfilename.txt] _____

mock_splitext = <MagicMock name='splitext' id='140639177084560'>
filename = 'longfilenamewithextension.txt', max_len = 15
expected = 'longfilename.txt'

    @pytest.mark.parametrize("filename, max_len, expected", [
        (None, 20, None),
        ("longfilenamewithextension.txt", 15, "longfilename.txt"),
        ("shortfile", 20, "shortfile"),
        ("anotherlongfile.with.many.dots.ext", 10, "anoth.ext")
    ])
    @patch('os.path.splitext')
    def test_trim_filename(mock_splitext, filename, max_len, expected):
        if filename is None:
            with pytest.raises(TypeError):
                trim_filename(filename, max_len)
        else:
            mock_splitext.return_value = ("name", "ext")
>           assert trim_filename(filename, max_len) == expected
E           AssertionError: assert 'longfilenamewit' == 'longfilename.txt'
E             
E             - longfilename.txt
E             ?             ^ --
E             + longfilenamewit
E             ?             ^^

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_trim_filename_1_test_edge_case_none.py:29: AssertionError
_____ test_trim_filename[anotherlongfile.with.many.dots.ext-10-anoth.ext] ______

mock_splitext = <MagicMock name='splitext' id='140639177371600'>
filename = 'anotherlongfile.with.many.dots.ext', max_len = 10
expected = 'anoth.ext'

    @pytest.mark.parametrize("filename, max_len, expected", [
        (None, 20, None),
        ("longfilenamewithextension.txt", 15, "longfilename.txt"),
        ("shortfile", 20, "shortfile"),
        ("anotherlongfile.with.many.dots.ext", 10, "anoth.ext")
    ])
    @patch('os.path.splitext')
    def test_trim_filename(mock_splitext, filename, max_len, expected):
        if filename is None:
            with pytest.raises(TypeError):
                trim_filename(filename, max_len)
        else:
            mock_splitext.return_value = ("name", "ext")
>           assert trim_filename(filename, max_len) == expected
E           AssertionError: assert 'anotherlon' == 'anoth.ext'
E             
E             - anoth.ext
E             + anotherlon

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_trim_filename_1_test_edge_case_none.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_trim_filename_1_test_edge_case_none.py::test_trim_filename[longfilenamewithextension.txt-15-longfilename.txt]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_trim_filename_1_test_edge_case_none.py::test_trim_filename[anotherlongfile.with.many.dots.ext-10-anoth.ext]
========================= 2 failed, 2 passed in 0.14s ==========================
"""