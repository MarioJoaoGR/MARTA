
import pytest
from dataclasses_json.core import _decode_letter_case_overrides

def test_edge_cases():
    # Test with None and empty lists
    assert _decode_letter_case_overrides([], {}) == {}
    assert _decode_letter_case_overrides(['FirstName'], None) == {}

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_3_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with None and empty lists
        assert _decode_letter_case_overrides([], {}) == {}
>       assert _decode_letter_case_overrides(['FirstName'], None) == {}

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_3_test_edge_cases.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_names = ['FirstName'], overrides = None

    def _decode_letter_case_overrides(field_names, overrides):
        """Override letter case of field names for encode/decode"""
        names = {}
        for field_name in field_names:
>           field_override = overrides.get(field_name)
E           AttributeError: 'NoneType' object has no attribute 'get'

dataclasses-json/dataclasses_json/core.py:148: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_letter_case_overrides_3_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.03s ===============================
"""