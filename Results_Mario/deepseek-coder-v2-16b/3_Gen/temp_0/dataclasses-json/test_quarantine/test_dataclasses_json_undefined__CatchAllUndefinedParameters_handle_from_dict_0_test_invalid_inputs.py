
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError

@pytest.fixture
def cls():
    @dataclass
    class TestClass:
        param1: int = 0
        param2: str = "default"
        catch_all: Dict[str, Any] = None

    return TestClass

def test_invalid_inputs(cls):
    kvs = {'param1': 1, 'catch_all': {'extra_param': 2}}
    with pytest.raises(UndefinedParameterError) as excinfo:
        _CatchAllUndefinedParameters.handle_from_dict(cls=cls, kvs=kvs)
    assert "Received input field with same name as catch-all field" in str(excinfo.value)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

cls = <class 'Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_invalid_inputs.cls.<locals>.TestClass'>

    def test_invalid_inputs(cls):
        kvs = {'param1': 1, 'catch_all': {'extra_param': 2}}
        with pytest.raises(UndefinedParameterError) as excinfo:
            _CatchAllUndefinedParameters.handle_from_dict(cls=cls, kvs=kvs)
>       assert "Received input field with same name as catch-all field" in str(excinfo.value)
E       AssertionError: assert 'Received input field with same name as catch-all field' in 'No field of type dataclasses_json.CatchAll defined'
E        +  where 'No field of type dataclasses_json.CatchAll defined' = str(UndefinedParameterError('No field of type dataclasses_json.CatchAll defined'))
E        +    where UndefinedParameterError('No field of type dataclasses_json.CatchAll defined') = <ExceptionInfo UndefinedParameterError('No field of type dataclasses_json.CatchAll defined') tblen=3>.value

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_invalid_inputs.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.05s ===============================
"""