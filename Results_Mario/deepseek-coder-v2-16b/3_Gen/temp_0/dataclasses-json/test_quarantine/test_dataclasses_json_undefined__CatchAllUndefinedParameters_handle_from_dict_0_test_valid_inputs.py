
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError

@pytest.fixture
def cls():
    class TestClass:
        pass
    return TestClass

@pytest.fixture
def kvs() -> Dict[str, Any]:
    return {'param1': 1, 'extra_param': 2}

def test_valid_inputs(cls, kvs):
    @dataclass
    class TestDataClass(_CatchAllUndefinedParameters):
        param1: int = None

    result = _CatchAllUndefinedParameters.handle_from_dict(cls=TestDataClass, kvs=kvs)
    assert 'param1' in result
    assert result['param1'] == 1
    assert 'extra_param' not in result

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

cls = <class 'Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_valid_inputs.cls.<locals>.TestClass'>
kvs = {'extra_param': 2, 'param1': 1}

    def test_valid_inputs(cls, kvs):
        @dataclass
        class TestDataClass(_CatchAllUndefinedParameters):
            param1: int = None
    
>       result = _CatchAllUndefinedParameters.handle_from_dict(cls=TestDataClass, kvs=kvs)

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_valid_inputs.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/undefined.py:138: in handle_from_dict
    catch_all_field = _CatchAllUndefinedParameters._get_catch_all_field(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_valid_inputs.test_valid_inputs.<locals>.TestDataClass'>

    @staticmethod
    def _get_catch_all_field(cls) -> Field:
        cls_globals = vars(sys.modules[cls.__module__])
        types = get_type_hints(cls, globalns=cls_globals)
        catch_all_fields = list(
            filter(lambda f: types[f.name] == Optional[CatchAllVar], fields(cls)))
        number_of_catch_all_fields = len(catch_all_fields)
        if number_of_catch_all_fields == 0:
>           raise UndefinedParameterError(
E           dataclasses_json.undefined.UndefinedParameterError: No field of type dataclasses_json.CatchAll defined

dataclasses-json/dataclasses_json/undefined.py:256: UndefinedParameterError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.04s ===============================
"""