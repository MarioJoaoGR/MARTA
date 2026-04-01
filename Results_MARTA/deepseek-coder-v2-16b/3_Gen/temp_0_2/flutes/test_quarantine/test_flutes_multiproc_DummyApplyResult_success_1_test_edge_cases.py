
import pytest
from flutes.multiproc import dummy_apply_result, DummyApplyResult

def test_dummy_apply_result():
    # Test creating a DummyApplyResult with an integer value
    result = dummy_apply_result(42)
    assert isinstance(result, DummyApplyResult)
    assert result._value == 42
    
    # Test creating a DummyApplyResult with a string value
    result = dummy_apply_result("hello")
    assert isinstance(result, DummyApplyResult)
    assert result._value == "hello"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_DummyApplyResult_success_1_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_DummyApplyResult_success_1_test_edge_cases.py:3:0: E0611: No name 'dummy_apply_result' in module 'flutes.multiproc' (no-name-in-module)


"""