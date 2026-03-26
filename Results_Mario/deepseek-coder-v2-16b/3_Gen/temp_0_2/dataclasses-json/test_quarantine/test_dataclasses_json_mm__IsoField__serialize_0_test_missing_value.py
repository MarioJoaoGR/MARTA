
import pytest
from dataclasses_json.mm import _IsoField, ValidationError

def test_missing_value():
    field = _IsoField(required=True)
    obj = type('Obj', (), {'required_field': None})()
    
    with pytest.raises(ValidationError) as exc_info:
        field._serialize(None, attr="required_field", obj=obj)
    
    assert str(exc_info.value) == '_IsoField.default_error_messages["required"]'

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_0_test_missing_value.py F [100%]

=================================== FAILURES ===================================
______________________________ test_missing_value ______________________________

    def test_missing_value():
        field = _IsoField(required=True)
        obj = type('Obj', (), {'required_field': None})()
    
        with pytest.raises(ValidationError) as exc_info:
            field._serialize(None, attr="required_field", obj=obj)
    
>       assert str(exc_info.value) == '_IsoField.default_error_messages["required"]'
E       assert 'Missing data...quired field.' == '_IsoField.de...s["required"]'
E         
E         - _IsoField.default_error_messages["required"]
E         + Missing data for required field.

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_0_test_missing_value.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_0_test_missing_value.py::test_missing_value
============================== 1 failed in 0.03s ===============================
"""