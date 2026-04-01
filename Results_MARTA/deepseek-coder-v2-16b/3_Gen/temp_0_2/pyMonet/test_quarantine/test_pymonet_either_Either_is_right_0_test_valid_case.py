
from pymonet.either import Either
import pytest

def test_valid_case():
    # Test when value is Right
    either = Either(5)
    assert either.is_right() == True
    
    # Test when value is Left
    either = Either(None)
    assert either.is_right() == False
    
    # Test with a string, which should be Right
    either = Either("example")
    assert either.is_right() == True

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        # Test when value is Right
        either = Either(5)
>       assert either.is_right() == True
E       assert None == True
E        +  where None = is_right()
E        +    where is_right = <pymonet.either.Either object at 0x7f0b15bb6c50>.is_right

pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_valid_case.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.08s ===============================
"""