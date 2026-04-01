
import pytest
from flutes.iterator import Range

def test_valid_case_one_argument():
    r = Range(10)
    assert isinstance(r, Range), "Instance should be of type Range"
    assert r[0] == 0, "Index 0 should return 0"
    assert r[2] == 2, "Index 2 should return 2"
    assert r[4] == 4, "Index 4 should return 4"
    with pytest.raises(IndexError):
        r[10]  # This should raise an IndexError

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

flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_valid_case_one_argument.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_case_one_argument _________________________

    def test_valid_case_one_argument():
        r = Range(10)
        assert isinstance(r, Range), "Instance should be of type Range"
        assert r[0] == 0, "Index 0 should return 0"
        assert r[2] == 2, "Index 2 should return 2"
        assert r[4] == 4, "Index 4 should return 4"
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_valid_case_one_argument.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_valid_case_one_argument.py::test_valid_case_one_argument
============================== 1 failed in 0.08s ===============================
"""