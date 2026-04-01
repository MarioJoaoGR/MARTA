
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _decode_type, _support_extended_types

@pytest.mark.parametrize("type_, value, infer_missing, expected", [
    (datetime, "2023-10-15", True, datetime(2023, 10, 15)),
    (Decimal, "123.45", True, Decimal('123.45')),
    (UUID, "123e4567-e89b-12d3-a456-426614174000", True, UUID('123e4567-e89b-12d3-a456-426614174000'))
])
def test_valid_case_datetime(type_, value, infer_missing, expected):
    assert _decode_type(type_, value, infer_missing) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_case_datetime.py F [ 33%]
..                                                                       [100%]

=================================== FAILURES ===================================
_________ test_valid_case_datetime[datetime-2023-10-15-True-expected0] _________

type_ = <class 'datetime.datetime'>, value = '2023-10-15', infer_missing = True
expected = datetime.datetime(2023, 10, 15, 0, 0)

    @pytest.mark.parametrize("type_, value, infer_missing, expected", [
        (datetime, "2023-10-15", True, datetime(2023, 10, 15)),
        (Decimal, "123.45", True, Decimal('123.45')),
        (UUID, "123e4567-e89b-12d3-a456-426614174000", True, UUID('123e4567-e89b-12d3-a456-426614174000'))
    ])
    def test_valid_case_datetime(type_, value, infer_missing, expected):
>       assert _decode_type(type_, value, infer_missing) == expected

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_case_datetime.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/core.py:250: in _decode_type
    return _support_extended_types(type_, value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_type = <class 'datetime.datetime'>, field_value = '2023-10-15'

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
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_case_datetime.py::test_valid_case_datetime[datetime-2023-10-15-True-expected0]
========================= 1 failed, 2 passed in 0.03s ==========================
"""