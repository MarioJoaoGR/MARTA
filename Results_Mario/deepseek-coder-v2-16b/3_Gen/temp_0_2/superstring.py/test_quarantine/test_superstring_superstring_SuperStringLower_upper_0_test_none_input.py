
import pytest
from superstring.superstring import SuperStringLower

def test_none_input():
    with pytest.raises(TypeError):
        ssu = SuperStringLower(None)  # Passing None to the constructor
        ssu.upper()  # Calling the upper method on the instance

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_upper_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(TypeError):
            ssu = SuperStringLower(None)  # Passing None to the constructor
>           ssu.upper()  # Calling the upper method on the instance

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_upper_0_test_none_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringLower object at 0x7f64b55ea290>

    def upper(self):
>       return self._base.upper()
E       AttributeError: 'NoneType' object has no attribute 'upper'

superstring.py/superstring/superstring.py:153: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_upper_0_test_none_input.py::test_none_input
============================== 1 failed in 0.05s ===============================
"""