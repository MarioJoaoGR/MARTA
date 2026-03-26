
import pytest
from dataclasses_json.core import _decode_dict_keys, _get_type_origin
from decimal import Decimal
from typing import Any, TypeVar, Tuple
from datetime import datetime, timezone
from unittest.mock import patch

@pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
    (int, {None: "value"}, False, {None: "value"}),  # Test with None keys
    (Decimal, {"123.45": "value"}, True, {Decimal('123.45'): "value"}),  # Test with Decimal keys inferred from string values
    (str, {}, False, {}),  # Test with empty dictionary and default key type str
    (None, {"key1": "value1", "key2": "value2"}, False, {"key1": "value1", "key2": "value2"}),  # Test with None as key_type
    (lambda x: x, {1: "value1", 2: "value2"}, False, {1: "value1", 2: "value2"}),  # Test with callable key type
])
def test_decode_dict_keys(key_type, xs, infer_missing, expected):
    with patch('dataclasses_json.core._get_type_origin', return_value=tuple if isinstance(key_type, Tuple) else key_type):
        result = _decode_dict_keys(key_type, xs, infer_missing)
        assert dict(result) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_edge_case.py F [ 20%]
F.FF                                                                     [100%]

=================================== FAILURES ===================================
________________ test_decode_dict_keys[int-xs0-False-expected0] ________________

key_type = <class 'int'>, xs = {None: 'value'}, infer_missing = False
expected = {None: 'value'}

    @pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
        (int, {None: "value"}, False, {None: "value"}),  # Test with None keys
        (Decimal, {"123.45": "value"}, True, {Decimal('123.45'): "value"}),  # Test with Decimal keys inferred from string values
        (str, {}, False, {}),  # Test with empty dictionary and default key type str
        (None, {"key1": "value1", "key2": "value2"}, False, {"key1": "value1", "key2": "value2"}),  # Test with None as key_type
        (lambda x: x, {1: "value1", 2: "value2"}, False, {1: "value1", 2: "value2"}),  # Test with callable key type
    ])
    def test_decode_dict_keys(key_type, xs, infer_missing, expected):
        with patch('dataclasses_json.core._get_type_origin', return_value=tuple if isinstance(key_type, Tuple) else key_type):
>           result = _decode_dict_keys(key_type, xs, infer_missing)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_edge_case.py:18: 
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

field_type = <class 'int'>, field_value = None

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
E           TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

dataclasses-json/dataclasses_json/core.py:274: TypeError
______________ test_decode_dict_keys[Decimal-xs1-True-expected1] _______________

key_type = <class 'decimal.Decimal'>, xs = {'123.45': 'value'}
infer_missing = True, expected = {Decimal('123.45'): 'value'}

    @pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
        (int, {None: "value"}, False, {None: "value"}),  # Test with None keys
        (Decimal, {"123.45": "value"}, True, {Decimal('123.45'): "value"}),  # Test with Decimal keys inferred from string values
        (str, {}, False, {}),  # Test with empty dictionary and default key type str
        (None, {"key1": "value1", "key2": "value2"}, False, {"key1": "value1", "key2": "value2"}),  # Test with None as key_type
        (lambda x: x, {1: "value1", 2: "value2"}, False, {1: "value1", 2: "value2"}),  # Test with callable key type
    ])
    def test_decode_dict_keys(key_type, xs, infer_missing, expected):
        with patch('dataclasses_json.core._get_type_origin', return_value=tuple if isinstance(key_type, Tuple) else key_type):
            result = _decode_dict_keys(key_type, xs, infer_missing)
>           assert dict(result) == expected
E           TypeError: cannot convert dictionary update sequence element #0 to a sequence

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_edge_case.py:19: TypeError
_______________ test_decode_dict_keys[None-xs3-False-expected3] ________________

key_type = None, xs = {'key1': 'value1', 'key2': 'value2'}
infer_missing = False, expected = {'key1': 'value1', 'key2': 'value2'}

    @pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
        (int, {None: "value"}, False, {None: "value"}),  # Test with None keys
        (Decimal, {"123.45": "value"}, True, {Decimal('123.45'): "value"}),  # Test with Decimal keys inferred from string values
        (str, {}, False, {}),  # Test with empty dictionary and default key type str
        (None, {"key1": "value1", "key2": "value2"}, False, {"key1": "value1", "key2": "value2"}),  # Test with None as key_type
        (lambda x: x, {1: "value1", 2: "value2"}, False, {1: "value1", 2: "value2"}),  # Test with callable key type
    ])
    def test_decode_dict_keys(key_type, xs, infer_missing, expected):
        with patch('dataclasses_json.core._get_type_origin', return_value=tuple if isinstance(key_type, Tuple) else key_type):
            result = _decode_dict_keys(key_type, xs, infer_missing)
>           assert dict(result) == expected
E           ValueError: dictionary update sequence element #0 has length 4; 2 is required

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_edge_case.py:19: ValueError
_____________ test_decode_dict_keys[<lambda>-xs4-False-expected4] ______________

key_type = <function <lambda> at 0x106342a70>, xs = {1: 'value1', 2: 'value2'}
infer_missing = False, expected = {1: 'value1', 2: 'value2'}

    @pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
        (int, {None: "value"}, False, {None: "value"}),  # Test with None keys
        (Decimal, {"123.45": "value"}, True, {Decimal('123.45'): "value"}),  # Test with Decimal keys inferred from string values
        (str, {}, False, {}),  # Test with empty dictionary and default key type str
        (None, {"key1": "value1", "key2": "value2"}, False, {"key1": "value1", "key2": "value2"}),  # Test with None as key_type
        (lambda x: x, {1: "value1", 2: "value2"}, False, {1: "value1", 2: "value2"}),  # Test with callable key type
    ])
    def test_decode_dict_keys(key_type, xs, infer_missing, expected):
        with patch('dataclasses_json.core._get_type_origin', return_value=tuple if isinstance(key_type, Tuple) else key_type):
            result = _decode_dict_keys(key_type, xs, infer_missing)
>           assert dict(result) == expected
E           TypeError: cannot convert dictionary update sequence element #0 to a sequence

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_edge_case.py:19: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_edge_case.py::test_decode_dict_keys[int-xs0-False-expected0]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_edge_case.py::test_decode_dict_keys[Decimal-xs1-True-expected1]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_edge_case.py::test_decode_dict_keys[None-xs3-False-expected3]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_edge_case.py::test_decode_dict_keys[<lambda>-xs4-False-expected4]
========================= 4 failed, 1 passed in 0.04s ==========================
"""