
from pymonet.utils import compose

def test_valid_input():
    def add_one(x): return x + 1
    def multiply_by_two(x): return x * 2
    
    assert compose(5, add_one, multiply_by_two) == 12

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

pyMonet/Test4DT_tests/test_pymonet_utils_compose_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        def add_one(x): return x + 1
        def multiply_by_two(x): return x * 2
    
>       assert compose(5, add_one, multiply_by_two) == 12
E       assert 11 == 12
E        +  where 11 = compose(5, <function test_valid_input.<locals>.add_one at 0x7f45fabc20c0>, <function test_valid_input.<locals>.multiply_by_two at 0x7f45fabc2340>)

pyMonet/Test4DT_tests/test_pymonet_utils_compose_0_test_valid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_compose_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""