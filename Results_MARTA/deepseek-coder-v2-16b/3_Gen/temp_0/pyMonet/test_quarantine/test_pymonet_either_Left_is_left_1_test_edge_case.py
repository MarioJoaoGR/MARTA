
from pymoneta.either import Left  # Correctly importing from the correct module

def test_edge_case():
    left = Left()
    assert left.is_left() is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_is_left_1_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_either_Left_is_left_1_test_edge_case.py:2:0: E0401: Unable to import 'pymoneta.either' (import-error)


"""