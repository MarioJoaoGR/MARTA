
import pytest
from superstring.superstring import SuperStringBase

def test_valid_input_direct_index():
    obj = SuperStringBase('Hello, World!')
    assert obj[0] == 'H'
    assert obj[1] == 'e'
    assert obj[7] == 'W'
    assert obj[-1] == '!'
    with pytest.raises(IndexError):
        obj[15]  # This should raise an IndexError since the string is only 13 characters long

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___getitem___0_test_valid_input_direct_index.py F [100%]

=================================== FAILURES ===================================
________________________ test_valid_input_direct_index _________________________

    def test_valid_input_direct_index():
>       obj = SuperStringBase('Hello, World!')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___getitem___0_test_valid_input_direct_index.py:6: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___getitem___0_test_valid_input_direct_index.py::test_valid_input_direct_index
============================== 1 failed in 0.04s ===============================
"""