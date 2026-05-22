
import pytest
from unittest.mock import patch
from httpie.downloads import get_filename_max_length, trim_filename

def test_trim_filename_if_needed():
    with patch('httpie.downloads.get_filename_max_length', return_value=20):
        assert trim_filename_if_needed("longfilenamewithextension.txt", extra=5) == "longfilenam.txt"
        assert trim_filename_if_needed("shortfile", extra=0) == "shortfile"
        assert trim_filename_if_needed("toolongfilename.ext", extra=3) == "toolon.ext"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_downloads_trim_filename_if_needed_0_test_edge_case_none
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_trim_filename_if_needed_0_test_edge_case_none.py:8:15: E0602: Undefined variable 'trim_filename_if_needed' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_trim_filename_if_needed_0_test_edge_case_none.py:9:15: E0602: Undefined variable 'trim_filename_if_needed' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_trim_filename_if_needed_0_test_edge_case_none.py:10:15: E0602: Undefined variable 'trim_filename_if_needed' (undefined-variable)


"""