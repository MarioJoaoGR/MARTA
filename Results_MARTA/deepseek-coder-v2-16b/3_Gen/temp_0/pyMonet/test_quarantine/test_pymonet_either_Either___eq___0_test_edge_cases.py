
from pymonet.either import Either, Left, Right

def test_edge_cases():
    # Test None value
    none_value = Either(Left(None))
    assert not none_value.is_right()
    
    # Test empty list
    empty_list = Either(Right([]))
    assert empty_list.is_right()

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

pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None value
        none_value = Either(Left(None))
        assert not none_value.is_right()
    
        # Test empty list
        empty_list = Either(Right([]))
>       assert empty_list.is_right()
E       assert None
E        +  where None = is_right()
E        +    where is_right = <pymonet.either.Either object at 0x7fc1139c3750>.is_right

pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___0_test_edge_cases.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.07s ===============================
"""