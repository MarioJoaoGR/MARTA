
import pytest
from dataclasses_json.core import _support_extended_types, _issubclass_safe
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID

def test_edge_cases():
    # Test None
    assert _support_extended_types(type(None), None) is None
    
    # Test empty list
    with pytest.raises(ValueError):  # Assuming the function raises ValueError for non-matching types
        _support_extended_types(int, [])

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None
        assert _support_extended_types(type(None), None) is None
    
        # Test empty list
        with pytest.raises(ValueError):  # Assuming the function raises ValueError for non-matching types
>           _support_extended_types(int, [])

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_0_test_edge_cases.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_type = <class 'int'>, field_value = []

    def _support_extended_types(field_type, field_value):
        if _issubclass_safe(field_type, datetime):
            # FIXME this is a hack to deal with mm already decoding
            # the issue is we want to leverage mm fields' missing argument
            # but need this for the object creation hook
            if isinstance(field_value, datetime):
                res = field_value
            else:
                tz = datetime.now(timezone.utc).astimezone().tzinfo
                res = datetime.fromtimestamp(field_value, tz=tz)
        elif _issubclass_safe(field_type, Decimal):
            res = (field_value
                   if isinstance(field_value, Decimal)
                   else Decimal(field_value))
        elif _issubclass_safe(field_type, UUID):
            res = (field_value
                   if isinstance(field_value, UUID)
                   else UUID(field_value))
        elif _issubclass_safe(field_type, (int, float, str, bool)):
            res = (field_value
                   if isinstance(field_value, field_type)
>                  else field_type(field_value))
E           TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

dataclasses-json/dataclasses_json/core.py:274: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.05s ===============================
"""