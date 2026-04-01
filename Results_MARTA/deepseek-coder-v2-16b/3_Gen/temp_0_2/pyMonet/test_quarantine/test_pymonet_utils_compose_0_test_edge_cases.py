
from pymonet.utils import compose, reduce
import pytest

def test_edge_cases():
    # Test None as input
    assert compose(None) is None
    
    # Test empty list of functions
    assert compose(5, []) == 5

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

pyMonet/Test4DT_tests/test_pymonet_utils_compose_0_test_edge_cases.py F  [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None as input
        assert compose(None) is None
    
        # Test empty list of functions
>       assert compose(5, []) == 5

pyMonet/Test4DT_tests/test_pymonet_utils_compose_0_test_edge_cases.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/utils.py:92: in compose
    return reduce(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

current_value = 5, function = []

>       lambda current_value, function: function(current_value),
        functions[::-1],
        value
    )
E   TypeError: 'list' object is not callable

pyMonet/pymonet/utils.py:93: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_compose_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.08s ===============================
"""