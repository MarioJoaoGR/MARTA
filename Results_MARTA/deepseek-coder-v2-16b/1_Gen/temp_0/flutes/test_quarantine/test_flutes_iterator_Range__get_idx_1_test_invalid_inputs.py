
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # No arguments provided
        r = Range()
    
    with pytest.raises(ValueError):
        # More than three arguments provided
        r = Range(1, 2, 3, 4)
    
    with pytest.raises(ValueError):
        # Only one argument provided (should be treated as 'end')
        r = Range(10)
    
    with pytest.raises(ValueError):
        # Two arguments without step specified
        r = Range(1, 2)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(ValueError):
            # No arguments provided
            r = Range()
    
        with pytest.raises(ValueError):
            # More than three arguments provided
            r = Range(1, 2, 3, 4)
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_invalid_inputs.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.09s ===============================
"""