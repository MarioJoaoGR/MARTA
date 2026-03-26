
from typing import Optional, List
import pytest
from dataclasses_json.utils import _is_optional

def test_valid_input_optional_class():
    # Test cases for valid optional classes
    assert _is_optional(Optional[int])  # True, since it's an Optional type with int as its argument.
    assert not _is_optional(List[int])   # False, even though List is a container, it doesn't represent an optional value directly.
    assert _is_optional(Optional)        # True, since it's the Optional type itself.

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_0_test_valid_input_optional_class.py F [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_optional_class ________________________

    def test_valid_input_optional_class():
        # Test cases for valid optional classes
        assert _is_optional(Optional[int])  # True, since it's an Optional type with int as its argument.
        assert not _is_optional(List[int])   # False, even though List is a container, it doesn't represent an optional value directly.
>       assert _is_optional(Optional)        # True, since it's the Optional type itself.
E       assert False
E        +  where False = _is_optional(Optional)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_0_test_valid_input_optional_class.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_0_test_valid_input_optional_class.py::test_valid_input_optional_class
============================== 1 failed in 0.03s ===============================
"""