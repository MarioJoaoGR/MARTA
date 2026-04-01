
import pytest
from dataclasses_json.core import _decode_dict_keys, _get_type_origin
from typing import TypeVar, Any, Tuple, Dict, List

def test_none_key_type():
    my_dict = {1: "value", (2, 3): "another value"}
    decoded_dict = _decode_dict_keys(None, my_dict, infer_missing=True)
    assert decoded_dict == {1: "value", (2, 3): "another value"}

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_none_key_type.py F [100%]

=================================== FAILURES ===================================
______________________________ test_none_key_type ______________________________

    def test_none_key_type():
        my_dict = {1: "value", (2, 3): "another value"}
        decoded_dict = _decode_dict_keys(None, my_dict, infer_missing=True)
>       assert decoded_dict == {1: "value", (2, 3): "another value"}
E       AssertionError: assert <map object at 0x1048d8d30> == {1: 'value', ...nother value'}
E         
E         Use -v to get more diff

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_none_key_type.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0_test_none_key_type.py::test_none_key_type
============================== 1 failed in 0.03s ===============================

"""