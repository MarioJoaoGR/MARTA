
import pytest
from isort._vendored.tomli._parser import skip_until, suffixed_err

def test_edge_case():
    with pytest.raises(suffixed_err) as excinfo:
        # This should raise an error because the substring 'xyz' does not exist in the source string
        skip_until("abcdef", 0, "xyz", error_on={' ', '\n'}, error_on_eof=True)
    assert str(excinfo.value) == "Expected 'xyz'"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
>       with pytest.raises(suffixed_err) as excinfo:
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_1_test_edge_case.py:6: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_until_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.12s ===============================
"""