
import pytest
from superstring.superstring import SuperString, SuperStringLower

def test_invalid_input():
    with pytest.raises(TypeError):
        s = 'not a valid string'
        lower_str = SuperStringLower(s)
        lower_str.length()

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_length_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
            s = 'not a valid string'
            lower_str = SuperStringLower(s)
>           lower_str.length()

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_length_2_test_invalid_input.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringLower object at 0x7f57a45944d0>

    def length(self):
>       return self._base.length()
E       AttributeError: 'str' object has no attribute 'length'

superstring.py/superstring/superstring.py:156: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_length_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.05s ===============================
"""