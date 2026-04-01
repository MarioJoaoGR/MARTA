
import pytest
from flutes.iterator import MapList

def test_edge_case():
    func = lambda x: x * 2
    lst_empty = []
    maplist_empty = MapList(func, lst_empty)
    
    assert len(maplist_empty) == 0, "Expected an empty list"
    
    with pytest.raises(TypeError):
        _ = maplist_empty[0]  # Accessing a non-existent index should raise a TypeError

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

flutes/Test4DT_tests/test_flutes_iterator_MapList___getitem___1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        func = lambda x: x * 2
        lst_empty = []
        maplist_empty = MapList(func, lst_empty)
    
        assert len(maplist_empty) == 0, "Expected an empty list"
    
        with pytest.raises(TypeError):
>           _ = maplist_empty[0]  # Accessing a non-existent index should raise a TypeError

flutes/Test4DT_tests/test_flutes_iterator_MapList___getitem___1_test_edge_case.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.MapList object at 0x7fb8ab058cd0>, item = 0

    def __getitem__(self, item):
        if isinstance(item, int):
>           return self.func(self.list[item])
E           IndexError: list index out of range

flutes/flutes/iterator.py:394: IndexError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_MapList___getitem___1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.09s ===============================
"""