
from pytutils.lazy.simple_import import NonLocal

def test_invalid_input():
    try:
        nl = NonLocal()  # This should raise a TypeError because value is not provided
    except TypeError as e:
        assert str(e) == "__init__() missing 1 required positional argument: 'value'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_simple_import_NonLocal___init___0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_NonLocal___init___0_test_invalid_input.py:6:13: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""