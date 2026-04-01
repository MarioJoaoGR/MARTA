
from functools import reduce
from pymonet.utils import compose

def test_compose_edge_cases():
    # Test with None as the initial value
    assert compose(None) is None
    
    # Test with an empty list of functions
    def add_one(x): return x + 1
    assert compose(5, add_one) == 6
    assert compose(5) == 5
    
    # Test with a function that returns None
    def noop(x): return None
    assert compose(5, noop) is None
    
    # Test with multiple functions
    def add_two(x): return x + 2
    def multiply_by_three(x): return x * 3
    result = compose(5, add_one, add_two, multiply_by_three)
    assert result == ((5 + 1 + 2) * 3)

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
___________________________ test_compose_edge_cases ____________________________

    def test_compose_edge_cases():
        # Test with None as the initial value
        assert compose(None) is None
    
        # Test with an empty list of functions
        def add_one(x): return x + 1
        assert compose(5, add_one) == 6
        assert compose(5) == 5
    
        # Test with a function that returns None
        def noop(x): return None
        assert compose(5, noop) is None
    
        # Test with multiple functions
        def add_two(x): return x + 2
        def multiply_by_three(x): return x * 3
        result = compose(5, add_one, add_two, multiply_by_three)
>       assert result == ((5 + 1 + 2) * 3)
E       assert 18 == (((5 + 1) + 2) * 3)

pyMonet/Test4DT_tests/test_pymonet_utils_compose_0_test_edge_cases.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_compose_0_test_edge_cases.py::test_compose_edge_cases
============================== 1 failed in 0.08s ===============================
"""