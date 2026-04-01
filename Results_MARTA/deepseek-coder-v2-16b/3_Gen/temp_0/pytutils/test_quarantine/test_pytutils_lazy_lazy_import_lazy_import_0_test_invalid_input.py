
from pytutils.lazy import lazy_import
import pytest

def test_invalid_input():
    with pytest.raises(TypeError):
        # Attempt to call lazy_import without providing scope or text
        lazy_import()

    with pytest.raises(TypeError):
        # Attempt to call lazy_import without providing any arguments
        lazy_import(scope={}, text="")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_lazy_import_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_lazy_import_0_test_invalid_input.py:8:8: E1102: lazy_import is not callable (not-callable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_lazy_import_0_test_invalid_input.py:12:8: E1102: lazy_import is not callable (not-callable)


"""