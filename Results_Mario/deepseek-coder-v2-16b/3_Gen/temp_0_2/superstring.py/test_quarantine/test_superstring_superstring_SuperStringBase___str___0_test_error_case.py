
import pytest
from superstring.superstring import SuperStringBase, SuperStringConcatenation

def test_error_case():
    s1 = SuperStringBase('Hello')
    s2 = SuperStringBase(', World!')
    concat_str = SuperStringConcatenation(s1, s2)
    
    with pytest.raises(ValueError):
        concat_str.to_printable(start_index=7, end_index=5)

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
>       s1 = SuperStringBase('Hello')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_error_case.py:6: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_error_case.py::test_error_case
============================== 1 failed in 0.04s ===============================
"""