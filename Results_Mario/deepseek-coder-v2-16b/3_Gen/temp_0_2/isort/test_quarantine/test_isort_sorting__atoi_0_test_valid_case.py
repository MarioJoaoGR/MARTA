
import re
from isort.sorting import _natural_keys

def test_valid_case():
    assert _natural_keys("a1b2c3") == [ord('a'), ord('1'), ord('b'), ord('2'), ord('c'), ord('3')]

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

isort/Test4DT_tests/test_isort_sorting__atoi_0_test_valid_case.py F      [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
>       assert _natural_keys("a1b2c3") == [ord('a'), ord('1'), ord('b'), ord('2'), ord('c'), ord('3')]
E       AssertionError: assert ['a', 1, 'b', 2, 'c', 3, ...] == [97, 49, 98, 50, 99, 51]
E         
E         At index 0 diff: 'a' != 97
E         Left contains one more item: ''
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_sorting__atoi_0_test_valid_case.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_sorting__atoi_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.09s ===============================
"""