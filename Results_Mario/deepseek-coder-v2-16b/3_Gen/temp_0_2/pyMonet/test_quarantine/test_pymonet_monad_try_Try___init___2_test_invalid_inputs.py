
import pytest
from pymonet.monad_try import Try

def test_invalid_inputs():
    # Test when value is None and is_success is False
    try_object = Try(None, False)
    assert not try_object.is_success
    assert try_object.value is None

    # Test when value is a string and is_success is True
    try_object = Try("result", True)
    assert try_object.is_success
    assert try_object.value == "result"

    # Test when value is an integer and is_success is False
    with pytest.raises(TypeError):  # Expecting a TypeError because of invalid input type
        Try(123, False)

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

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try___init___2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test when value is None and is_success is False
        try_object = Try(None, False)
        assert not try_object.is_success
        assert try_object.value is None
    
        # Test when value is a string and is_success is True
        try_object = Try("result", True)
        assert try_object.is_success
        assert try_object.value == "result"
    
        # Test when value is an integer and is_success is False
>       with pytest.raises(TypeError):  # Expecting a TypeError because of invalid input type
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try___init___2_test_invalid_inputs.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_monad_try_Try___init___2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.10s ===============================
"""