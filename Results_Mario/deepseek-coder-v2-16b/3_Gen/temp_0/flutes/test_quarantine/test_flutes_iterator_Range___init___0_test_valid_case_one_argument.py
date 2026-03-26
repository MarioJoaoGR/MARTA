
import pytest
from flutes.iterator import Range

def test_valid_case_one_argument():
    r = Range(10)
    assert isinstance(r, Range)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.length == 10
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4
    assert r[9] == 9

    with pytest.raises(IndexError):
        r[10]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_valid_case_one_argument.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_case_one_argument _________________________

    def test_valid_case_one_argument():
        r = Range(10)
        assert isinstance(r, Range)
        assert r.l == 0
        assert r.r == 10
        assert r.step == 1
        assert r.length == 10
        assert r[0] == 0
        assert r[2] == 2
        assert r[4] == 4
        assert r[9] == 9
    
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_valid_case_one_argument.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_valid_case_one_argument.py::test_valid_case_one_argument
============================== 1 failed in 0.11s ===============================
"""