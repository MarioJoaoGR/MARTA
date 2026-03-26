
import pytest
from flutes.iterator import Range

def test_valid_case_two_args():
    r = Range(1, 10)
    assert r._get_idx(0) == 1
    assert r._get_idx(1) == 3

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_valid_case_two_args.py F [100%]

=================================== FAILURES ===================================
___________________________ test_valid_case_two_args ___________________________

    def test_valid_case_two_args():
        r = Range(1, 10)
        assert r._get_idx(0) == 1
>       assert r._get_idx(1) == 3
E       assert 2 == 3
E        +  where 2 = _get_idx(1)
E        +    where _get_idx = <flutes.iterator.Range object at 0x7f9e211a1050>._get_idx

flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_valid_case_two_args.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range__get_idx_1_test_valid_case_two_args.py::test_valid_case_two_args
============================== 1 failed in 0.10s ===============================

"""