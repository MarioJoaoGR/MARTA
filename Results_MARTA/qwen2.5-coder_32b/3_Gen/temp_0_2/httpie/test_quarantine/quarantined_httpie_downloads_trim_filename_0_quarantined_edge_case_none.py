
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

@patch('os.path.splitext')
def test_trim_filename(mock_splitext):
    mock_splitext.return_value = ("name", "ext")
    
    assert trim_filename("longfilenamewithextension.txt", 15) == "longfilename.txt"
    assert trim_filename("shortfile", 20) == "shortfile"
    assert trim_filename("anotherlongfile.with.many.dots.ext", 10) == "anoth.ext"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_trim_filename_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
______________________________ test_trim_filename ______________________________

mock_splitext = <MagicMock name='splitext' id='140710305265296'>

    @patch('os.path.splitext')
    def test_trim_filename(mock_splitext):
        mock_splitext.return_value = ("name", "ext")
    
>       assert trim_filename("longfilenamewithextension.txt", 15) == "longfilename.txt"
E       AssertionError: assert 'longfilenamewit' == 'longfilename.txt'
E         
E         - longfilename.txt
E         ?             ^ --
E         + longfilenamewit
E         ?             ^^

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_trim_filename_0_test_edge_case_none.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_trim_filename_0_test_edge_case_none.py::test_trim_filename
============================== 1 failed in 0.12s ===============================
"""