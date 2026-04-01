
import pytest
from dataclasses_json.core import _decode_dict_keys, _decode_items, _decode_type, _support_extended_types
from decimal import Decimal
from datetime import datetime, timezone
from typing import Any, TypeVar, Tuple

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test case for invalid key type (not a callable or None)
        _decode_dict_keys("invalid_type", {}, True)
    
    with pytest.raises(TypeError):
        # Test case for invalid dictionary input (not a dict)
        _decode_dict_keys(int, "invalid_input", True)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
            # Test case for invalid key type (not a callable or None)
            _decode_dict_keys("invalid_type", {}, True)
    
        with pytest.raises(TypeError):
            # Test case for invalid dictionary input (not a dict)
>           _decode_dict_keys(int, "invalid_input", True)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/core.py:373: in _decode_dict_keys
    return map(decode_function, _decode_items(key_type, xs, infer_missing))
dataclasses-json/dataclasses_json/core.py:410: in _decode_items
    return list(_decode_type(type_args, x, infer_missing) for x in xs)
dataclasses-json/dataclasses_json/core.py:410: in <genexpr>
    return list(_decode_type(type_args, x, infer_missing) for x in xs)
dataclasses-json/dataclasses_json/core.py:250: in _decode_type
    return _support_extended_types(type_, value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_type = <class 'int'>, field_value = 'i'

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
E           ValueError: invalid literal for int() with base 10: 'i'

dataclasses-json/dataclasses_json/core.py:274: ValueError
=============================== warnings summary ===============================
Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_input.py::test_invalid_input
  /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/dataclasses_json/core.py:394: UserWarning: Could not resolve self-reference for type invalid_type, decoded type might be incorrect or decode might fail altogether.
    warnings.warn(f"Could not resolve self-reference for type {pre_0673_hint}, "

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_input.py::test_invalid_input
========================= 1 failed, 1 warning in 0.05s =========================
"""