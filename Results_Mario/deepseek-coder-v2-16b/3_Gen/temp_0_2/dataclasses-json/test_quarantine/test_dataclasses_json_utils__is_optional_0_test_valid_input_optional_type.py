
from typing import Optional
import pytest
from dataclasses_json.utils import _is_optional

def test_valid_input_optional_type():
    # Test cases for valid optional types
    assert _is_optional(Optional[int]) == True  # True, since it's an Optional type with int as its argument.
    assert _is_optional(Optional) == True        # True, since it's the Optional type itself.

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_0_test_valid_input_optional_type.py F [100%]

=================================== FAILURES ===================================
________________________ test_valid_input_optional_type ________________________

    def test_valid_input_optional_type():
        # Test cases for valid optional types
        assert _is_optional(Optional[int]) == True  # True, since it's an Optional type with int as its argument.
>       assert _is_optional(Optional) == True        # True, since it's the Optional type itself.
E       assert False == True
E        +  where False = _is_optional(Optional)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_0_test_valid_input_optional_type.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_optional_0_test_valid_input_optional_type.py::test_valid_input_optional_type
============================== 1 failed in 0.03s ===============================
"""