
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import _IgnoreUndefinedParameters

class Test_IgnoreUndefinedParameters:
    @dataclass
    class ExampleClass:
        param1: int
        param2: str

    def test_handle_from_dict_invalid_inputs(self):
        with pytest.raises(TypeError) as excinfo:
            _IgnoreUndefinedParameters.handle_from_dict(cls=Test_IgnoreUndefinedParameters.ExampleClass, kvs={'extra_param': 'value'})
        assert str(excinfo.value) == 'handle_from_dict() takes 2 positional arguments but 3 were given'

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____ Test_IgnoreUndefinedParameters.test_handle_from_dict_invalid_inputs ______

self = <Test4DT_tests.test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_invalid_inputs.Test_IgnoreUndefinedParameters object at 0x101ff1b40>

    def test_handle_from_dict_invalid_inputs(self):
>       with pytest.raises(TypeError) as excinfo:
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_invalid_inputs.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_invalid_inputs.py::Test_IgnoreUndefinedParameters::test_handle_from_dict_invalid_inputs
============================== 1 failed in 0.03s ===============================

"""