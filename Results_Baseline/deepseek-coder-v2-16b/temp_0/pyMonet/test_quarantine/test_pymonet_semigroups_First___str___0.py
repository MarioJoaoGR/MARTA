
# Module: pymonet.semigroups
# test_monet.py
from pymonet.semigroups import First
import pytest

@pytest.fixture
def first1():
    return First(5)

@pytest.fixture
def first2():
    return First(10)

def test_first_initialization():
    first = First(5)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_First___str___0
pyMonet/Test4DT_tests/test_pymonet_semigroups_First___str___0.py:19:43: E0001: Parsing failed: 'expected an indented block after function definition on line 19 (Test4DT_tests.test_pymonet_semigroups_First___str___0, line 19)' (syntax-error)


"""