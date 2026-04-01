
import pytest
from flutes.structure import map_structure_zip
from typing import Callable, Collection, Sequence, TypeVar

R = TypeVar('R')
T = TypeVar('T')

def test_error_case_invalid_input():
    with pytest.raises(ValueError):
        # Test case for invalid input where structures contain `set` which is unordered
        map_structure_zip(lambda x, y: x + y, [(1, 2), {3, 4}])

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

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_error_case_invalid_input.py F [100%]

=================================== FAILURES ===================================
________________________ test_error_case_invalid_input _________________________

    def test_error_case_invalid_input():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_error_case_invalid_input.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_error_case_invalid_input.py::test_error_case_invalid_input
============================== 1 failed in 0.10s ===============================
"""