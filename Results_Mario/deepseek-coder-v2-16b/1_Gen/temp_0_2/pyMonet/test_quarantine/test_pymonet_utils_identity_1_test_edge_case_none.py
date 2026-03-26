
import pytest

def identity(value: T) -> T:
    """
    Return first argument.

    :param value:
    :type value: Any
    :returns:
    :rtype: Any
    """
    return value

def test_edge_case_none():
    with pytest.raises(TypeError):
        identity(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_identity_1_test_edge_case_none
pyMonet/Test4DT_tests/test_pymonet_utils_identity_1_test_edge_case_none.py:4:20: E0602: Undefined variable 'T' (undefined-variable)
pyMonet/Test4DT_tests/test_pymonet_utils_identity_1_test_edge_case_none.py:4:26: E0602: Undefined variable 'T' (undefined-variable)


"""