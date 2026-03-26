
import pytest
from dataclasses import dataclass, fields, is_dataclass
from dataclasses_json.undefined import _catch_all_init as original_init
from dataclasses_json.undefined import _CatchAllUndefinedParameters

@pytest.fixture
def setup_class():
    @dataclass
    class MyClass:
        def __init__(self, *args, **kwargs):
            _catch_all_init(self, *args, **kwargs)
    
    return MyClass

def test_edge_cases(setup_class):
    cls = setup_class()
    obj = cls(1, 2, param1="value1", unknown_param="unknown_value")
    
    assert hasattr(obj, 'param1')
    assert getattr(obj, 'param1') == "value1"
    assert not hasattr(obj, 'unknown_param')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__catch_all_init_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__catch_all_init_0_test_edge_cases.py:4:0: E0611: No name '_catch_all_init' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__catch_all_init_0_test_edge_cases.py:12:12: E0602: Undefined variable '_catch_all_init' (undefined-variable)


"""