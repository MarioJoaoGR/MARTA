
import pytest
from isort.exceptions import LiteralSortTypeMismatch

def test_edge_cases():
    # Test with None values
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(None, int)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'NoneType'>."

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

isort/Test4DT_tests/test_isort_exceptions_LiteralSortTypeMismatch___init___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with None values
        with pytest.raises(LiteralSortTypeMismatch) as excinfo:
            raise LiteralSortTypeMismatch(None, int)
>       assert str(excinfo.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'NoneType'>."
E       assert 'isort was to...of type None.' == "isort was to... 'NoneType'>."
E         
E         Skipping 77 identical leading characters in diff, use -v to show
E         - l of type <class 'NoneType'>.
E         + l of type None.

isort/Test4DT_tests/test_isort_exceptions_LiteralSortTypeMismatch___init___1_test_edge_cases.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_LiteralSortTypeMismatch___init___1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.10s ===============================
"""