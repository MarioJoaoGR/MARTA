
import pytest
from superstring import SuperStringBase

def test_character_at():
    s = SuperStringBase("Hello, world!")
    assert s.character_at(0) == 'H'
    assert s.character_at(7) == ','
    assert s.character_at(12) == '!'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringBase_character_at_0_test_edge_case
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_character_at_0_test_edge_case.py:3:0: E0611: No name 'SuperStringBase' in module 'superstring' (no-name-in-module)


"""