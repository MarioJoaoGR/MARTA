
from pymonet.semigroups import Min

def test_valid_inputs():
    min_monoid = Min()
    
    assert str(min_monoid) == 'Min[value=inf]'
    assert min_monoid.combine(5, 3) == 3
    assert min_monoid.combine(-1, 0) == -1
    assert min_monoid.combine(2, 2) == 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Min___str___0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_semigroups_Min___str___0_test_valid_inputs.py:5:17: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)
pyMonet/Test4DT_tests/test_pymonet_semigroups_Min___str___0_test_valid_inputs.py:8:11: E1101: Instance of 'Min' has no 'combine' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_semigroups_Min___str___0_test_valid_inputs.py:9:11: E1101: Instance of 'Min' has no 'combine' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_semigroups_Min___str___0_test_valid_inputs.py:10:11: E1101: Instance of 'Min' has no 'combine' member (no-member)


"""