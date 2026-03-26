
import pytest
from isort.sorting import _atoi

def test_valid_input():
    assert _atoi("123") == 123
    assert _atoi("0") == 0
    assert _atoi("456789") == 456789
    with pytest.raises(ValueError):
        _atoi("abc")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_sorting__atoi_0_test_valid_input.py F     [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        assert _atoi("123") == 123
        assert _atoi("0") == 0
        assert _atoi("456789") == 456789
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort_sorting__atoi_0_test_valid_input.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_sorting__atoi_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.11s ===============================
"""