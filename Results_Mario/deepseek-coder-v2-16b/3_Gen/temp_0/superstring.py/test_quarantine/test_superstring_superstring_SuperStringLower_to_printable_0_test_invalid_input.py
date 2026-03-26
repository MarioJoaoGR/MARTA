
import pytest
from superstring.superstring import SuperStringLower

def test_invalid_input():
    with pytest.raises(TypeError):
        s = SuperStringLower('Hello, World!')
        s.to_printable()  # This should raise a TypeError because the method expects optional parameters to be integers or None

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
            s = SuperStringLower('Hello, World!')
>           s.to_printable()  # This should raise a TypeError because the method expects optional parameters to be integers or None

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringLower object at 0x7ff763901950>
start_index = None, end_index = None

    def to_printable(self, start_index=None, end_index=None):
>       return self._base.to_printable(start_index, end_index).lower()
E       AttributeError: 'str' object has no attribute 'to_printable'

superstring.py/superstring/superstring.py:162: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================
"""