
from pymonet.semigroups import Map

def test_valid_input():
    map_instance = Map()
    map_instance.value = [1, 2, 3]
    assert str(map_instance) == 'Map[value=[1, 2, 3]]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Map___str___0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_semigroups_Map___str___0_test_valid_input.py:5:19: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""