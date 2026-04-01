
import pytest
from superstring.superstring import SuperStringBase

def test_valid_input_integer_index():
    s = SuperStringBase('Hello, World!')
    assert s[7] == 'W'
    assert s.character_at(7) == 'W'

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___getitem___0_test_valid_input_integer_index.py F [100%]

=================================== FAILURES ===================================
________________________ test_valid_input_integer_index ________________________

    def test_valid_input_integer_index():
>       s = SuperStringBase('Hello, World!')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___getitem___0_test_valid_input_integer_index.py:6: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___getitem___0_test_valid_input_integer_index.py::test_valid_input_integer_index
============================== 1 failed in 0.04s ===============================
"""