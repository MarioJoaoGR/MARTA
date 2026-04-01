
from typing import Optional, List, Union
import pytest
from dataclasses_json.utils import _is_optional

def test_invalid_case_non_optional_type():
    # Test cases where the type is not optional
    assert not _is_optional(int)  # Basic non-optional type
    assert not _is_optional(str)  # Basic non-optional type
    assert not _is_optional(List[int])  # List is not optional
    assert not _is_optional(Union[int, None])  # Union with None is not optional

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_1_test_invalid_case_non_optional_type.py F [100%]

=================================== FAILURES ===================================
_____________________ test_invalid_case_non_optional_type ______________________

    def test_invalid_case_non_optional_type():
        # Test cases where the type is not optional
        assert not _is_optional(int)  # Basic non-optional type
        assert not _is_optional(str)  # Basic non-optional type
        assert not _is_optional(List[int])  # List is not optional
>       assert not _is_optional(Union[int, None])  # Union with None is not optional
E       assert not True
E        +  where True = _is_optional(typing.Optional[int])

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_1_test_invalid_case_non_optional_type.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_1_test_invalid_case_non_optional_type.py::test_invalid_case_non_optional_type
============================== 1 failed in 0.04s ===============================
"""