
import pytest
from flutes.multiproc import DummyPool

def test_invalid_inputs():
    pool = DummyPool(processes=0)  # Create a DummyPool instance
    
    # Test with a non-callable function to raise TypeError
    with pytest.raises(TypeError):
        result = pool.imap_unordered(None, [1, 2, 3])  # Passing None which is not callable

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

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        pool = DummyPool(processes=0)  # Create a DummyPool instance
    
        # Test with a non-callable function to raise TypeError
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_1_test_invalid_inputs.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.09s ===============================
"""