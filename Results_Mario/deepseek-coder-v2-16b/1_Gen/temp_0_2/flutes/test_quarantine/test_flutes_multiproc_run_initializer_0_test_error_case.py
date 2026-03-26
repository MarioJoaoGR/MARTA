
import pytest
from flutes.multiproc import initializer

def test_error_case():
    with pytest.raises(NameError):
        run_initializer()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_run_initializer_0_test_error_case
flutes/Test4DT_tests/test_flutes_multiproc_run_initializer_0_test_error_case.py:3:0: E0611: No name 'initializer' in module 'flutes.multiproc' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_run_initializer_0_test_error_case.py:7:8: E0602: Undefined variable 'run_initializer' (undefined-variable)


"""