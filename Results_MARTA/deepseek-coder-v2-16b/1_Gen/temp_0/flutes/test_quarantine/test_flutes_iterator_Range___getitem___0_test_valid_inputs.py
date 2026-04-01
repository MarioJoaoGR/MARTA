
from flutes.iterator import Range

def test_negative_index():
    r = Range(10)
    assert r[-1] == 9
    assert r[-3] == 7
    assert r[-5] == 5
    
    r = Range(1, 10 + 1)
    assert r[-1] == 10
    assert r[-3] == 8
    assert r[-5] == 6
    
    r = Range(1, 11, 2)
    assert r[-1] == 9
    assert r[-3] == 7
    assert r[-5] == 5

def test_slice():
    r = Range(10)
    assert r[slice(0, len(r), 2)] == [0, 2, 4, 6, 8]
    
    r = Range(1, 10 + 1)
    assert r[slice(0, len(r), 2)] == [1, 3, 5, 7, 9]
    
    r = Range(1, 11, 2)
    assert r[slice(0, len(r), 2)] == [1, 3, 5, 7, 9]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_inputs.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_negative_index ______________________________

    def test_negative_index():
        r = Range(10)
        assert r[-1] == 9
        assert r[-3] == 7
        assert r[-5] == 5
    
        r = Range(1, 10 + 1)
        assert r[-1] == 10
        assert r[-3] == 8
        assert r[-5] == 6
    
        r = Range(1, 11, 2)
        assert r[-1] == 9
>       assert r[-3] == 7
E       assert 5 == 7

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_inputs.py:17: AssertionError
__________________________________ test_slice __________________________________

    def test_slice():
        r = Range(10)
        assert r[slice(0, len(r), 2)] == [0, 2, 4, 6, 8]
    
        r = Range(1, 10 + 1)
        assert r[slice(0, len(r), 2)] == [1, 3, 5, 7, 9]
    
        r = Range(1, 11, 2)
>       assert r[slice(0, len(r), 2)] == [1, 3, 5, 7, 9]
E       assert [1, 5, 9] == [1, 3, 5, 7, 9]
E         
E         At index 1 diff: 5 != 3
E         Right contains 2 more items, first extra item: 7
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_inputs.py:28: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_inputs.py::test_negative_index
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___getitem___0_test_valid_inputs.py::test_slice
============================== 2 failed in 0.09s ===============================
"""