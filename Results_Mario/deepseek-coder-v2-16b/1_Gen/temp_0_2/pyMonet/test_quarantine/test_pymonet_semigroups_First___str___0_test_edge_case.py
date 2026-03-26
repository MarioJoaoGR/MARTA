
from pymonet.semigroups import First

def test_str_representation():
    # Test when value is not provided
    first_instance = First()
    assert str(first_instance) == 'Fist[value=]'
    
    # Test with a specific value
    first1 = First(value=1)
    first2 = First(value=2)
    combined = first1 + first2  # This will always return the value from first1, which is 1.
    assert str(combined) == 'Fist[value=1]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_First___str___0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_semigroups_First___str___0_test_edge_case.py:6:21: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""