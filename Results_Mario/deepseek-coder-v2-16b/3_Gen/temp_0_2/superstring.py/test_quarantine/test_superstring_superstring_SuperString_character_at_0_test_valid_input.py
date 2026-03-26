
import pytest
from superstring.superstring import SuperString

def test_valid_input():
    s = SuperString('Hello, World!')
    assert s.split() == ['Hello,', 'World!']

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_character_at_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        s = SuperString('Hello, World!')
>       assert s.split() == ['Hello,', 'World!']
E       AssertionError: assert [<superstring...7fa639a12b10>] == ['Hello,', 'World!']
E         
E         At index 0 diff: <superstring.superstring.SuperString object at 0x7fa63a75e650> != 'Hello,'
E         Use -v to get more diff

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_character_at_0_test_valid_input.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_character_at_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""