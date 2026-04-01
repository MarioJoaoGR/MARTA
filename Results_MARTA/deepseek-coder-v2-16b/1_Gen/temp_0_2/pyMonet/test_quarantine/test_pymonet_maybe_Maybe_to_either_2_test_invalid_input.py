
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_invalid_input():
    with pytest.raises(Exception):
        maybe = Maybe(value=42, is_nothing=False)  # Creating a Maybe instance with a value
        either = maybe.to_either()  # Transforming to Either
        
        assert isinstance(either, Right)  # Assert that the result is of type Right
        assert either.value == 42  # Assert that the contained value is correct

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_either_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_either_2_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_either_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.06s ===============================
"""