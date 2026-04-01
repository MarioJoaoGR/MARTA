
import pytest
from dataclasses_json.core import _decode_type, is_dataclass, _support_extended_types, _has_decoder_in_global_config, _get_decoder_in_global_config
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID

@pytest.mark.parametrize("type_, value, infer_missing", [
    (int, "notanumber", False),  # Invalid int input
    (float, "notafloat", False),  # Invalid float input
    (str, 123, False),            # Invalid str input
    (bool, "true", False),        # Invalid bool input
    (datetime, "invalid_date", False),  # Invalid datetime input
    (Decimal, "notadecimal", False),   # Invalid Decimal input
    (UUID, "notauuid", False),       # Invalid UUID input
])
def test_invalid_inputs(type_, value, infer_missing):
    with pytest.raises(ValueError):  # Expecting a ValueError for invalid inputs
        _decode_type(type_, value, infer_missing)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 7 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_inputs.py . [ 14%]
.FFFF.                                                                   [100%]

=================================== FAILURES ===================================
______________________ test_invalid_inputs[str-123-False] ______________________

type_ = <class 'str'>, value = 123, infer_missing = False

    @pytest.mark.parametrize("type_, value, infer_missing", [
        (int, "notanumber", False),  # Invalid int input
        (float, "notafloat", False),  # Invalid float input
        (str, 123, False),            # Invalid str input
        (bool, "true", False),        # Invalid bool input
        (datetime, "invalid_date", False),  # Invalid datetime input
        (Decimal, "notadecimal", False),   # Invalid Decimal input
        (UUID, "notauuid", False),       # Invalid UUID input
    ])
    def test_invalid_inputs(type_, value, infer_missing):
>       with pytest.raises(ValueError):  # Expecting a ValueError for invalid inputs
E       Failed: DID NOT RAISE <class 'ValueError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_inputs.py:18: Failed
_____________________ test_invalid_inputs[bool-true-False] _____________________

type_ = <class 'bool'>, value = 'true', infer_missing = False

    @pytest.mark.parametrize("type_, value, infer_missing", [
        (int, "notanumber", False),  # Invalid int input
        (float, "notafloat", False),  # Invalid float input
        (str, 123, False),            # Invalid str input
        (bool, "true", False),        # Invalid bool input
        (datetime, "invalid_date", False),  # Invalid datetime input
        (Decimal, "notadecimal", False),   # Invalid Decimal input
        (UUID, "notauuid", False),       # Invalid UUID input
    ])
    def test_invalid_inputs(type_, value, infer_missing):
>       with pytest.raises(ValueError):  # Expecting a ValueError for invalid inputs
E       Failed: DID NOT RAISE <class 'ValueError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_inputs.py:18: Failed
_______________ test_invalid_inputs[datetime-invalid_date-False] _______________

type_ = <class 'datetime.datetime'>, value = 'invalid_date'
infer_missing = False

    @pytest.mark.parametrize("type_, value, infer_missing", [
        (int, "notanumber", False),  # Invalid int input
        (float, "notafloat", False),  # Invalid float input
        (str, 123, False),            # Invalid str input
        (bool, "true", False),        # Invalid bool input
        (datetime, "invalid_date", False),  # Invalid datetime input
        (Decimal, "notadecimal", False),   # Invalid Decimal input
        (UUID, "notauuid", False),       # Invalid UUID input
    ])
    def test_invalid_inputs(type_, value, infer_missing):
        with pytest.raises(ValueError):  # Expecting a ValueError for invalid inputs
>           _decode_type(type_, value, infer_missing)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_inputs.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/core.py:250: in _decode_type
    return _support_extended_types(type_, value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_type = <class 'datetime.datetime'>, field_value = 'invalid_date'

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
________________ test_invalid_inputs[Decimal-notadecimal-False] ________________

type_ = <class 'decimal.Decimal'>, value = 'notadecimal', infer_missing = False

    @pytest.mark.parametrize("type_, value, infer_missing", [
        (int, "notanumber", False),  # Invalid int input
        (float, "notafloat", False),  # Invalid float input
        (str, 123, False),            # Invalid str input
        (bool, "true", False),        # Invalid bool input
        (datetime, "invalid_date", False),  # Invalid datetime input
        (Decimal, "notadecimal", False),   # Invalid Decimal input
        (UUID, "notauuid", False),       # Invalid UUID input
    ])
    def test_invalid_inputs(type_, value, infer_missing):
        with pytest.raises(ValueError):  # Expecting a ValueError for invalid inputs
>           _decode_type(type_, value, infer_missing)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_inputs.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/core.py:250: in _decode_type
    return _support_extended_types(type_, value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_type = <class 'decimal.Decimal'>, field_value = 'notadecimal'

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
>                  else Decimal(field_value))
E           decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>]

dataclasses-json/dataclasses_json/core.py:266: InvalidOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_inputs.py::test_invalid_inputs[str-123-False]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_inputs.py::test_invalid_inputs[bool-true-False]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_inputs.py::test_invalid_inputs[datetime-invalid_date-False]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_inputs.py::test_invalid_inputs[Decimal-notadecimal-False]
========================= 4 failed, 3 passed in 0.05s ==========================
"""