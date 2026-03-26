
import pytest
from decimal import Decimal
from typing import List, Collection
from dataclasses_json.core import _decode_items, _decode_type
from datetime import datetime, timezone
import sys
import warnings

@pytest.mark.parametrize("type_args, xs, infer_missing", [
    (List[int], ["1", "2"], False),  # Invalid input type for List[int]
    ([Decimal]*2, ['not a number', 'also not a number'], True),  # Invalid string inputs for Decimal*2
])
def test_invalid_input(type_args, xs, infer_missing):
    with pytest.raises(TypeError):
        _decode_items(type_args, xs, infer_missing)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_items_1_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input[List-xs0-False] ______________________

type_args = typing.List[int], xs = ['1', '2'], infer_missing = False

    @pytest.mark.parametrize("type_args, xs, infer_missing", [
        (List[int], ["1", "2"], False),  # Invalid input type for List[int]
        ([Decimal]*2, ['not a number', 'also not a number'], True),  # Invalid string inputs for Decimal*2
    ])
    def test_invalid_input(type_args, xs, infer_missing):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_items_1_test_invalid_input.py:15: Failed
___________________ test_invalid_input[type_args1-xs1-True] ____________________

type_args = [<class 'decimal.Decimal'>, <class 'decimal.Decimal'>]
xs = ['not a number', 'also not a number'], infer_missing = True

    @pytest.mark.parametrize("type_args, xs, infer_missing", [
        (List[int], ["1", "2"], False),  # Invalid input type for List[int]
        ([Decimal]*2, ['not a number', 'also not a number'], True),  # Invalid string inputs for Decimal*2
    ])
    def test_invalid_input(type_args, xs, infer_missing):
        with pytest.raises(TypeError):
>           _decode_items(type_args, xs, infer_missing)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_items_1_test_invalid_input.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/core.py:404: in _decode_items
    return list(_decode_type(type_arg, x, infer_missing) for type_arg, x in zip(type_args, xs))
dataclasses-json/dataclasses_json/core.py:404: in <genexpr>
    return list(_decode_type(type_arg, x, infer_missing) for type_arg, x in zip(type_args, xs))
dataclasses-json/dataclasses_json/core.py:250: in _decode_type
    return _support_extended_types(type_, value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

field_type = <class 'decimal.Decimal'>, field_value = 'not a number'

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
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_items_1_test_invalid_input.py::test_invalid_input[List-xs0-False]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_items_1_test_invalid_input.py::test_invalid_input[type_args1-xs1-True]
============================== 2 failed in 0.04s ===============================
"""