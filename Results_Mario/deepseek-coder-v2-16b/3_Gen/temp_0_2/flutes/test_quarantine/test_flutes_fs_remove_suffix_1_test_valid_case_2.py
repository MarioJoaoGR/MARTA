
import pytest
from flutes.fs import remove_suffix

def test_valid_case_2():
    s = 'https://github.com/huzecong/flutes'
    suffix = 'flutes'
    assert remove_suffix(s, suffix, fully_match=False) == "https://github.com/huzecong"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_valid_case_2.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
        s = 'https://github.com/huzecong/flutes'
        suffix = 'flutes'
>       assert remove_suffix(s, suffix, fully_match=False) == "https://github.com/huzecong"
E       AssertionError: assert 'https://github.com/huzecong/' == 'https://github.com/huzecong'
E         
E         - https://github.com/huzecong
E         + https://github.com/huzecong/
E         ?                            +

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_valid_case_2.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_valid_case_2.py::test_valid_case_2
============================== 1 failed in 0.08s ===============================
"""