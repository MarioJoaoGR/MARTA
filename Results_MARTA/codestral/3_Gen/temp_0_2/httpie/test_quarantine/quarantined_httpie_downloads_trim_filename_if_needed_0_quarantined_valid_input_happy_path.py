
import pytest
from unittest.mock import patch
from httpie.downloads import trim_filename_if_needed, get_filename_max_length

@pytest.mark.parametrize("filename, directory, extra, expected", [
    ("longfilenamewithextension.txt", "/home/user", 0, "longfilenamewithextension.txt"),
    ("longfilenamewithextension.txt", "/home/user", 5, "longfilenam.txt"),
    ("shortfile", "/home/user", 0, "shortfile")
])
def test_valid_input_happy_path(filename, directory, extra, expected):
    with patch('httpie.downloads.get_filename_max_length', return_value=255):
        assert trim_filename_if_needed(filename, directory, extra) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_if_needed_0_test_valid_input_happy_path.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_ test_valid_input_happy_path[longfilenamewithextension.txt-/home/user-5-longfilenam.txt] _

filename = 'longfilenamewithextension.txt', directory = '/home/user', extra = 5
expected = 'longfilenam.txt'

    @pytest.mark.parametrize("filename, directory, extra, expected", [
        ("longfilenamewithextension.txt", "/home/user", 0, "longfilenamewithextension.txt"),
        ("longfilenamewithextension.txt", "/home/user", 5, "longfilenam.txt"),
        ("shortfile", "/home/user", 0, "shortfile")
    ])
    def test_valid_input_happy_path(filename, directory, extra, expected):
        with patch('httpie.downloads.get_filename_max_length', return_value=255):
>           assert trim_filename_if_needed(filename, directory, extra) == expected
E           AssertionError: assert 'longfilename...extension.txt' == 'longfilenam.txt'
E             
E             - longfilenam.txt
E             + longfilenamewithextension.txt

httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_if_needed_0_test_valid_input_happy_path.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_downloads_trim_filename_if_needed_0_test_valid_input_happy_path.py::test_valid_input_happy_path[longfilenamewithextension.txt-/home/user-5-longfilenam.txt]
========================= 1 failed, 2 passed in 0.17s ==========================
"""