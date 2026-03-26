
import pytest
from pymonet.lazy import Lazy

def test_invalid_inputs():
    # Test that bind method raises TypeError when fn is not callable
    lazy_value = Lazy(lambda x: x * 2)  # Example valid constructor function
    
    with pytest.raises(TypeError):
        lazy_value.bind(lambda x: 'not a callable')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test that bind method raises TypeError when fn is not callable
        lazy_value = Lazy(lambda x: x * 2)  # Example valid constructor function
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_invalid_inputs.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.09s ===============================
"""