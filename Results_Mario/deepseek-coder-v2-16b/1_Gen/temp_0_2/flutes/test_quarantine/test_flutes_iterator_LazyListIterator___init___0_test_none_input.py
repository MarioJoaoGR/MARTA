
import pytest
from flutes.iterator import LazyListIterator

def test_none_input():
    with pytest.raises(TypeError):
        LazyListIterator(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyListIterator___init___0_test_none_input
flutes/Test4DT_tests/test_flutes_iterator_LazyListIterator___init___0_test_none_input.py:3:0: E0611: No name 'LazyListIterator' in module 'flutes.iterator' (no-name-in-module)


"""