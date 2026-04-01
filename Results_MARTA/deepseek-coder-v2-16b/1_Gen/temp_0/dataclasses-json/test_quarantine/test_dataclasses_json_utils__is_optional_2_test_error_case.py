
from typing import Optional, List, Any
import pytest
from dataclasses_json.utils import _is_optional, _issubclass_safe, _hasargs

def test_error_case():
    assert not _is_optional(int), "Expected int to return False"
    assert not _is_optional(str), "Expected str to return False"
    assert not _is_optional(List[int]), "Expected List[int] to return False"
    assert not _is_optional(Any), "Expected Any to return False"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_2_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        assert not _is_optional(int), "Expected int to return False"
        assert not _is_optional(str), "Expected str to return False"
        assert not _is_optional(List[int]), "Expected List[int] to return False"
>       assert not _is_optional(Any), "Expected Any to return False"
E       AssertionError: Expected Any to return False
E       assert not True
E        +  where True = _is_optional(Any)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_2_test_error_case.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_2_test_error_case.py::test_error_case
============================== 1 failed in 0.03s ===============================

"""