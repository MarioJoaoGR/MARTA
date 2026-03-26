
from pymonet.either import Either, Left, Right
from pymonet.box import Box

def test_edge_case():
    # Create an Either instance with a Right value
    either_instance = Either(Right("success"))
    
    # Transform it to a Box monad
    box_instance = either_instance.to_box()
    
    # Assert that the transformed Box instance contains the same value as the original Either instance
    assert isinstance(box_instance, Box)
    assert box_instance.value == "success"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Create an Either instance with a Right value
        either_instance = Either(Right("success"))
    
        # Transform it to a Box monad
        box_instance = either_instance.to_box()
    
        # Assert that the transformed Box instance contains the same value as the original Either instance
        assert isinstance(box_instance, Box)
>       assert box_instance.value == "success"
E       AssertionError: assert <pymonet.either.Right object at 0x7fa4730873d0> == 'success'
E        +  where <pymonet.either.Right object at 0x7fa4730873d0> = <pymonet.box.Box object at 0x7fa473068f10>.value

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_edge_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.06s ===============================
"""