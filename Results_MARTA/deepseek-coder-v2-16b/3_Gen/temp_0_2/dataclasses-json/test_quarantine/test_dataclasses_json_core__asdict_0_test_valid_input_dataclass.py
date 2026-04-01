
import pytest
from dataclasses import dataclass, fields
from typing import Collection, Mapping, Union, Dict, List
import copy
from dataclasses_json.core import _asdict, is_dataclass, _user_overrides_or_exts, _handle_undefined_parameters_safe, _encode_overrides, _has_encoder_in_global_config, _get_encoder_in_global_config
from dataclasses import asdict
import json

@dataclass
class Person:
    name: str
    age: int

def test_encode_json_true():
    data = [{"key": "value"}, {"another_key": "another_value"}]
    result = _asdict(data, encode_json=True)
    expected = [{'key': {'key': 'value'}}, {'another_key': {'another_key': 'another_value'}}]
    assert result == expected

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_valid_input_dataclass.py F [100%]

=================================== FAILURES ===================================
____________________________ test_encode_json_true _____________________________

    def test_encode_json_true():
        data = [{"key": "value"}, {"another_key": "another_value"}]
        result = _asdict(data, encode_json=True)
        expected = [{'key': {'key': 'value'}}, {'another_key': {'another_key': 'another_value'}}]
>       assert result == expected
E       AssertionError: assert [{'key': 'val...other_value'}] == [{'key': {'ke...ther_value'}}]
E         
E         At index 0 diff: {'key': 'value'} != {'key': {'key': 'value'}}
E         Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_valid_input_dataclass.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_valid_input_dataclass.py::test_encode_json_true
============================== 1 failed in 0.02s ===============================
"""