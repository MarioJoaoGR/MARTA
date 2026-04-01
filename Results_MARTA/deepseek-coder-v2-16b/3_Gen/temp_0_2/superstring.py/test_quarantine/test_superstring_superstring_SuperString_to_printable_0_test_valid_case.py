
import pytest
from superstring.superstring import SuperString

def test_valid_case():
    s = SuperString('Hello, World!')
    s2 = SuperString('Python')
    empty_string = SuperString('')
    
    assert s.split() == ['Hello,', 'World!']
    assert s2.split() == ['Python']
    assert empty_string.split() == []

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_to_printable_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        s = SuperString('Hello, World!')
        s2 = SuperString('Python')
        empty_string = SuperString('')
    
>       assert s.split() == ['Hello,', 'World!']
E       AssertionError: assert [<superstring...7f1a21cb2d10>] == ['Hello,', 'World!']
E         
E         At index 0 diff: <superstring.superstring.SuperString object at 0x7f1a21cb1c10> != 'Hello,'
E         Use -v to get more diff

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_to_printable_0_test_valid_case.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_to_printable_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.04s ===============================
"""