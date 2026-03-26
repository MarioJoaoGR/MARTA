
import pytest
from superstring.superstring import SuperString

def test_invalid_inputs():
    s = SuperString("Hello, world!")
    
    # Test when start_index is negative
    with pytest.raises(IndexError):
        s.substring(-1)

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString___init___0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        s = SuperString("Hello, world!")
    
        # Test when start_index is negative
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString___init___0_test_invalid_inputs.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperString___init___0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.04s ===============================
"""