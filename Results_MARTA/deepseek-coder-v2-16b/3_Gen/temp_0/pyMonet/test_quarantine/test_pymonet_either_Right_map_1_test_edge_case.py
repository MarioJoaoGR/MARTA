
import pytest
from pymonet.either import Right

def test_edge_case():
    right_none = Right(None)
    
    # Test that mapping over a None value does not raise an exception and returns a new Right instance with None
    mapped_right = right_none.map(lambda x: x + 1)
    assert isinstance(mapped_right, Right)
    assert mapped_right.value is None

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

pyMonet/Test4DT_tests/test_pymonet_either_Right_map_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        right_none = Right(None)
    
        # Test that mapping over a None value does not raise an exception and returns a new Right instance with None
>       mapped_right = right_none.map(lambda x: x + 1)

pyMonet/Test4DT_tests/test_pymonet_either_Right_map_1_test_edge_case.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/either.py:162: in map
    return Right(mapper(self.value))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = None

>   mapped_right = right_none.map(lambda x: x + 1)
E   TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

pyMonet/Test4DT_tests/test_pymonet_either_Right_map_1_test_edge_case.py:9: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Right_map_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.07s ===============================
"""