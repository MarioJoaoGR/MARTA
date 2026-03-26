
from pytutils.lazy.simple_import import simple_import

# Assuming 'NonLocal' class definition is in a module named 'pytutils'
nonlocal = simple_import('pytutils.NonLocal')

def test_valid_input():
    nl = nonlocal(10)
    assert nl.value == 10
    nl.value = 20
    assert nl.value == 20

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_simple_import_NonLocal___init___0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_NonLocal___init___0_test_valid_input.py:5:10: E0001: Parsing failed: 'invalid syntax (Test4DT_tests.test_pytutils_lazy_simple_import_NonLocal___init___0_test_valid_input, line 5)' (syntax-error)


"""