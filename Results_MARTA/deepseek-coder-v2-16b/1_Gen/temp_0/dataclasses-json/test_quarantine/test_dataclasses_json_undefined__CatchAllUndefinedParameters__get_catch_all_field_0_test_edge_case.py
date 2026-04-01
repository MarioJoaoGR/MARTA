
import pytest
from dataclasses import dataclass, fields
from typing import Optional
from dataclasses_json import CatchAllVar, UndefinedParameterError
import sys

@pytest.fixture(name="cls")
def fixture_cls():
    @dataclass
    class ExampleClass:
        field1: str
        field2: int
        utils_catchall: Optional[CatchAllVar] = None
    
    return ExampleClass

def test_get_catch_all_field(cls):
    cls_globals = vars(sys.modules[cls.__module__])
    types = get_type_hints(cls, globalns=cls_globals)
    catch_all_fields = list(filter(lambda f: types[f.name] == Optional[CatchAllVar], fields(cls)))
    
    assert len(catch_all_fields) == 1, "Expected exactly one catch-all field"
    
    catch_all_field = catch_all_fields[0]
    assert isinstance(catch_all_field.name, str), "Catch-all field should have a name"
    assert types[catch_all_field.name] == Optional[CatchAllVar], "Type hint for catch-all field is incorrect"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_catch_all_field_0_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_catch_all_field_0_test_edge_case.py:5:0: E0611: No name 'CatchAllVar' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_catch_all_field_0_test_edge_case.py:5:0: E0611: No name 'UndefinedParameterError' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_catch_all_field_0_test_edge_case.py:20:12: E0602: Undefined variable 'get_type_hints' (undefined-variable)

"""