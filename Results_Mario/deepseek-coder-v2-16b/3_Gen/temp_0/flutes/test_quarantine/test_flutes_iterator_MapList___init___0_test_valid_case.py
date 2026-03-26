
import pytest
from flutes.iterator import MapList

def test_valid_case():
    func = lambda x: x * x
    lst = [1, 2, 3, 4, 5]
    
    maplist = MapList(func, lst)
    
    # Check the transformed list
    assert list(maplist) == [1, 4, 9, 16, 25]
    
    # Find index of the first element in `lst` whose square is >= 10
    pos = bisect.bisect_left(maplist, 10)
    assert pos == 3

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_MapList___init___0_test_valid_case
flutes/Test4DT_tests/test_flutes_iterator_MapList___init___0_test_valid_case.py:15:10: E0602: Undefined variable 'bisect' (undefined-variable)


"""