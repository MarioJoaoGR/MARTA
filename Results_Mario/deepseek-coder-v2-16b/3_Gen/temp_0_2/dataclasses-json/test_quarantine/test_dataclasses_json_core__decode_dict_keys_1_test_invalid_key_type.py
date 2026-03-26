
import pytest
from dataclasses_json.core import _decode_dict_keys
from typing import Any, TypeVar, Union

@pytest.mark.parametrize("invalid_key_type", [None, "str", 123])
def test_invalid_key_type(invalid_key_type):
    with pytest.raises(TypeError):
        _decode_dict_keys(invalid_key_type, {}, False)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_key_type.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_key_type[None] __________________________

invalid_key_type = None

    @pytest.mark.parametrize("invalid_key_type", [None, "str", 123])
    def test_invalid_key_type(invalid_key_type):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_key_type.py:8: Failed
__________________________ test_invalid_key_type[str] __________________________

invalid_key_type = 'str'

    @pytest.mark.parametrize("invalid_key_type", [None, "str", 123])
    def test_invalid_key_type(invalid_key_type):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_key_type.py:8: Failed
__________________________ test_invalid_key_type[123] __________________________

invalid_key_type = 123

    @pytest.mark.parametrize("invalid_key_type", [None, "str", 123])
    def test_invalid_key_type(invalid_key_type):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_key_type.py:8: Failed
=============================== warnings summary ===============================
Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_key_type.py::test_invalid_key_type[str]
  /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/dataclasses_json/core.py:390: UserWarning: Assuming hint str resolves to <class 'str'> This is not necessarily the value that is in-scope.
    warnings.warn(f"Assuming hint {pre_0673_hint} resolves to {maybe_resolved} "

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_key_type.py::test_invalid_key_type[None]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_key_type.py::test_invalid_key_type[str]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_invalid_key_type.py::test_invalid_key_type[123]
========================= 3 failed, 1 warning in 0.03s =========================
"""