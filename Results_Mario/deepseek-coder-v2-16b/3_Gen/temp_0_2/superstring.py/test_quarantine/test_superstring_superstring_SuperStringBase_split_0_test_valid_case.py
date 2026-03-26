
import pytest
from superstring.superstring import SuperStringBase

def test_valid_case():
    base_string = SuperStringBase('Hello, World!')
    assert base_string is not None
    assert base_string.character_at(7) == 'W'
    substring = base_string.substring(7, 12)
    assert substring == 'World'
    split_result = base_string.split(", ")
    assert split_result == ['Hello', 'World!']

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_split_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
>       base_string = SuperStringBase('Hello, World!')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_split_0_test_valid_case.py:6: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_split_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.04s ===============================
"""