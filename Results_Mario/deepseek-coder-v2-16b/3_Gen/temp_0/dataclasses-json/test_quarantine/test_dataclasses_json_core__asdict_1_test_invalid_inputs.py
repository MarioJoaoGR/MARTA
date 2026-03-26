
import pytest
from dataclasses import dataclass, fields
from typing import Union, Mapping, Collection, List, Dict
import copy
from enum import Enum
from dataclasses_json.core import _asdict, is_dataclass, _user_overrides_or_exts, _handle_undefined_parameters_safe, _encode_overrides, _has_encoder_in_global_config, _get_encoder_in_global_config

@pytest.mark.parametrize("obj, encode_json", [
    ({"name": "John Doe", "age": 30}, False),
    ([1, "string", {"nestedKey": None}], True)
])
def test_invalid_inputs(obj: Union[dataclass, Mapping], encode_json: bool):
    result = _asdict(obj, encode_json=encode_json)
    assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_1_test_invalid_inputs.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_invalid_inputs[obj1-True] ________________________

obj = [1, 'string', {'nestedKey': None}], encode_json = True

    @pytest.mark.parametrize("obj, encode_json", [
        ({"name": "John Doe", "age": 30}, False),
        ([1, "string", {"nestedKey": None}], True)
    ])
    def test_invalid_inputs(obj: Union[dataclass, Mapping], encode_json: bool):
        result = _asdict(obj, encode_json=encode_json)
>       assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"
E       AssertionError: Expected a dictionary but got <class 'list'>
E       assert False
E        +  where False = isinstance([1, 'string', {'nestedKey': None}], dict)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_1_test_invalid_inputs.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_1_test_invalid_inputs.py::test_invalid_inputs[obj1-True]
========================= 1 failed, 1 passed in 0.03s ==========================
"""