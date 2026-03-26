
from pymonet.either import Right

def test_is_right():
    r = Right()
    assert r.is_right() is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Right_is_right_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_either_Right_is_right_0_test_edge_case.py:5:8: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""