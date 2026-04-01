
import pytest
from flutes.iterator import MapList

def test_valid_input():
    func = lambda x: x * x
    lst = [1, 2, 3, 4, 5]
    maplist = MapList(func, lst)
    
    # Test indexing access
    assert maplist[0] == 1
    assert maplist[1] == 4
    assert maplist[2] == 9
    assert maplist[3] == 16
    assert maplist[4] == 25
    
    # Test slicing access
    assert list(maplist[:]) == [1, 4, 9, 16, 25]
    assert list(maplist[1:]) == [4, 9, 16, 25]
    assert list(maplist[:3]) == [1, 4, 9]
    assert list(maplist[1:4]) == [4, 9, 16]
    
    # Test invalid index access raises IndexError
    with pytest.raises(IndexError):
        maplist[5]
    with pytest.raises(IndexError):
        maplist[-1]
    with pytest.raises(IndexError):
        maplist[10]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_MapList___getitem___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        func = lambda x: x * x
        lst = [1, 2, 3, 4, 5]
        maplist = MapList(func, lst)
    
        # Test indexing access
        assert maplist[0] == 1
        assert maplist[1] == 4
        assert maplist[2] == 9
        assert maplist[3] == 16
        assert maplist[4] == 25
    
        # Test slicing access
        assert list(maplist[:]) == [1, 4, 9, 16, 25]
        assert list(maplist[1:]) == [4, 9, 16, 25]
        assert list(maplist[:3]) == [1, 4, 9]
        assert list(maplist[1:4]) == [4, 9, 16]
    
        # Test invalid index access raises IndexError
        with pytest.raises(IndexError):
            maplist[5]
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_MapList___getitem___0_test_valid_input.py:26: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_MapList___getitem___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""