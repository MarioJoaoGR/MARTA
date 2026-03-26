
import pytest
from dataclasses import dataclass, fields
from typing import Union, Mapping, Collection, Dict, List
from dataclasses_json.core import _asdict

@pytest.mark.parametrize("obj", [123, "string", None])
def test_invalid_input_type(obj):
    with pytest.raises(TypeError):
        _asdict(obj)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_invalid_input_type.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_input_type[123] _________________________

obj = 123

    @pytest.mark.parametrize("obj", [123, "string", None])
    def test_invalid_input_type(obj):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_invalid_input_type.py:9: Failed
_______________________ test_invalid_input_type[string] ________________________

obj = 'string'

    @pytest.mark.parametrize("obj", [123, "string", None])
    def test_invalid_input_type(obj):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_invalid_input_type.py:9: Failed
________________________ test_invalid_input_type[None] _________________________

obj = None

    @pytest.mark.parametrize("obj", [123, "string", None])
    def test_invalid_input_type(obj):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_invalid_input_type.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_invalid_input_type.py::test_invalid_input_type[123]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_invalid_input_type.py::test_invalid_input_type[string]
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__asdict_0_test_invalid_input_type.py::test_invalid_input_type[None]
============================== 3 failed in 0.03s ===============================
"""