
from pymonet.either import Either, Left, Right
from pymonet.monad_try import Try
import pytest

def test_valid_input():
    either = Either(10)  # Creating an instance of Either with a value of 10
    try_instance = either.to_try()  # Converting Either to Try
    
    assert isinstance(try_instance, Try)
    assert not try_instance.is_success(), "Expected the Try instance to be in failure state"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        either = Either(10)  # Creating an instance of Either with a value of 10
        try_instance = either.to_try()  # Converting Either to Try
    
        assert isinstance(try_instance, Try)
>       assert not try_instance.is_success(), "Expected the Try instance to be in failure state"
E       TypeError: 'NoneType' object is not callable

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_valid_input.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""