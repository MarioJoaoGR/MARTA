
import re
from typing import Any
from isort.sorting import _natural_keys

def test_valid_input():
    assert _natural_keys("file123.txt") == ['file', 123, '.txt']
    assert _natural_keys("section4subsection5") == ['section', 4, 'subsection', 5]

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

isort/Test4DT_tests/test_isort_sorting__natural_keys_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        assert _natural_keys("file123.txt") == ['file', 123, '.txt']
>       assert _natural_keys("section4subsection5") == ['section', 4, 'subsection', 5]
E       AssertionError: assert ['section', 4...ction', 5, ''] == ['section', 4...ubsection', 5]
E         
E         Left contains one more item: ''
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_sorting__natural_keys_0_test_valid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_sorting__natural_keys_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""