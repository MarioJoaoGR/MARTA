
import pytest
from superstring import SuperStringBase

def test_character_at_valid_input():
    superstring_instance = SuperStringBase("Hello World")
    assert superstring_instance.character_at(0) == 'h'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringBase_character_at_0_test_valid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_character_at_0_test_valid_input.py:3:0: E0611: No name 'SuperStringBase' in module 'superstring' (no-name-in-module)


"""