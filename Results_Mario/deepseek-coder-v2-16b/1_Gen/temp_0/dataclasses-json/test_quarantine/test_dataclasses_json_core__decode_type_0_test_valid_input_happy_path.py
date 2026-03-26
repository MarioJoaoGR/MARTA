
import pytest
from datetime import datetime, timezone
from dataclasses_json.core import _decode_type, _support_extended_types, is_dataclass

def test_valid_input_happy_path():
    field_type = datetime
    field_value = "2023-10-05T12:00:00"  # A string representing a specific date and time
    res = _decode_type(field_type, field_value, infer_missing=True)
    
    assert isinstance(res, datetime), f"Expected datetime object, but got {type(res)}"
    assert str(res) == "2023-10-05 12:00:00", f"Expected date to be parsed correctly, but got {str(res)}"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        field_type = datetime
        field_value = "2023-10-05T12:00:00"  # A string representing a specific date and time
>       res = _decode_type(field_type, field_value, infer_missing=True)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_input_happy_path.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/core.py:250: in _decode_type
    return _support_extended_types(type_, value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_type = <class 'datetime.datetime'>, field_value = '2023-10-05T12:00:00'

    def _support_extended_types(field_type, field_value):
        if _issubclass_safe(field_type, datetime):
            # FIXME this is a hack to deal with mm already decoding
            # the issue is we want to leverage mm fields' missing argument
            # but need this for the object creation hook
            if isinstance(field_value, datetime):
                res = field_value
            else:
                tz = datetime.now(timezone.utc).astimezone().tzinfo
>               res = datetime.fromtimestamp(field_value, tz=tz)
E               TypeError: 'str' object cannot be interpreted as an integer

dataclasses-json/dataclasses_json/core.py:262: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.04s ===============================

"""