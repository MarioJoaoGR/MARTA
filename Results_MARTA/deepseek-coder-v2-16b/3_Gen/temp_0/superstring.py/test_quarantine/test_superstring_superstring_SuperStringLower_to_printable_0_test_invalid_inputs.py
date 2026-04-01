
import pytest
from superstring.superstring import SuperStringLower

def test_invalid_inputs():
    s = SuperStringLower("Hello, World!")
    
    # Test when start_index is greater than end_index
    with pytest.raises(ValueError):
        assert s.to_printable(start_index=5, end_index=3)

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        s = SuperStringLower("Hello, World!")
    
        # Test when start_index is greater than end_index
        with pytest.raises(ValueError):
>           assert s.to_printable(start_index=5, end_index=3)

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringLower object at 0x7f2d3c435b90>
start_index = 5, end_index = 3

    def to_printable(self, start_index=None, end_index=None):
>       return self._base.to_printable(start_index, end_index).lower()
E       AttributeError: 'str' object has no attribute 'to_printable'

superstring.py/superstring/superstring.py:162: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.05s ===============================
"""