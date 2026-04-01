
import pytest
from flutes.lazylist import LazyList
from flutes.iterator import LazyListIterator

def test_empty_list():
    lazy_list = LazyList()
    iterator = LazyListIterator(lazy_list)
    
    with pytest.raises(StopIteration):
        next(iterator)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_LazyListIterator___next___0_test_empty_list
flutes/Test4DT_tests/test_flutes_iterator_LazyListIterator___next___0_test_empty_list.py:3:0: E0401: Unable to import 'flutes.lazylist' (import-error)
flutes/Test4DT_tests/test_flutes_iterator_LazyListIterator___next___0_test_empty_list.py:3:0: E0611: No name 'lazylist' in module 'flutes' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_iterator_LazyListIterator___next___0_test_empty_list.py:4:0: E0611: No name 'LazyListIterator' in module 'flutes.iterator' (no-name-in-module)


"""