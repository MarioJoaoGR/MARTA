
from superstring.superstring import SuperStringBase, SuperStringUpper

def test_valid_case_with_specified_indices():
    u = SuperStringUpper(SuperStringBase('Python'))
    assert str(u) == 'PYTHON'
    assert u.to_printable(1, 4) == 'YTH'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_valid_case_with_specified_indices.py F [100%]

=================================== FAILURES ===================================
____________________ test_valid_case_with_specified_indices ____________________

    def test_valid_case_with_specified_indices():
>       u = SuperStringUpper(SuperStringBase('Python'))
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_valid_case_with_specified_indices.py:5: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_valid_case_with_specified_indices.py::test_valid_case_with_specified_indices
============================== 1 failed in 0.04s ===============================
"""