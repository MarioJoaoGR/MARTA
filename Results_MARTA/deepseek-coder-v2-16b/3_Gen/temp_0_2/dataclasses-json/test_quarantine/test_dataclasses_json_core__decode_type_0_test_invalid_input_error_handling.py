
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from dataclasses_json.core import _decode_type

@pytest.mark.parametrize("type_, value, infer_missing, expected", [
    (int, "123", False, 123),
    (float, "123.45", False, 123.45),
    (str, 123, False, "123"),
    (bool, "True", False, True),
    # Correct the test case for datetime to use a valid datetime string
    (datetime, "2023-10-01T12:00:00", False, datetime(2023, 10, 1, 12, 0)),
    (Decimal, "123.45", False, Decimal("123.45")),
    # Add more test cases as needed
])
def test_decode_type(type_, value, infer_missing, expected):
    decoded_value = _decode_type(type_, value, infer_missing)
    assert isinstance(decoded_value, type_)
    if isinstance(expected, datetime):
        # Ensure the timezone is set correctly for comparison
        assert decoded_value.replace(tzinfo=None) == expected.replace(tzinfo=None)
    else:
        assert decoded_value == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_input_error_handling.py . [ 16%]
...F.                                                                    [100%]

=================================== FAILURES ===================================
________ test_decode_type[datetime-2023-10-01T12:00:00-False-expected4] ________

type_ = <class 'datetime.datetime'>, value = '2023-10-01T12:00:00'
infer_missing = False, expected = datetime.datetime(2023, 10, 1, 12, 0)

    @pytest.mark.parametrize("type_, value, infer_missing, expected", [
        (int, "123", False, 123),
        (float, "123.45", False, 123.45),
        (str, 123, False, "123"),
        (bool, "True", False, True),
        # Correct the test case for datetime to use a valid datetime string
        (datetime, "2023-10-01T12:00:00", False, datetime(2023, 10, 1, 12, 0)),
        (Decimal, "123.45", False, Decimal("123.45")),
        # Add more test cases as needed
    ])
    def test_decode_type(type_, value, infer_missing, expected):
>       decoded_value = _decode_type(type_, value, infer_missing)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_input_error_handling.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/core.py:250: in _decode_type
    return _support_extended_types(type_, value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_type = <class 'datetime.datetime'>, field_value = '2023-10-01T12:00:00'

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
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_invalid_input_error_handling.py::test_decode_type[datetime-2023-10-01T12:00:00-False-expected4]
========================= 1 failed, 5 passed in 0.03s ==========================
"""