
import pytest
from superstring.superstring import SuperStringUpper

def test_none_input():
    with pytest.raises(TypeError):
        str_upper = SuperStringUpper(None)
        lower_str = str_upper.lower()

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_lower_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(TypeError):
            str_upper = SuperStringUpper(None)
>           lower_str = str_upper.lower()

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_lower_1_test_none_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringUpper object at 0x7f1d2a13dd50>

    def lower(self):
>       return self._base.lower()
E       AttributeError: 'NoneType' object has no attribute 'lower'

superstring.py/superstring/superstring.py:170: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_lower_1_test_none_input.py::test_none_input
============================== 1 failed in 0.05s ===============================
"""