
import pytest
from dataclasses_json.undefined import CatchAllVar, UndefinedParameterError
from typing import Optional, Any, Dict
from dataclasses import dataclass

# Assuming utils is a module that contains CatchAll and other necessary classes
# from dataclasses_json.utils import CatchAll  # Uncomment this line if utils exists in the actual code

@dataclass
class ExampleClass:
    field1: str
    field2: int
    utils.CatchAll = None  # Assuming this is the only catch-all field in the class

def test_invalid_inputs():
    with pytest.raises(UndefinedParameterError):
        obj = ExampleClass(field1="test", field2=123)
        _CatchAllUndefinedParameters.handle_dump(obj)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_dump_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_dump_0_test_invalid_inputs.py:14:4: E0602: Undefined variable 'utils' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_dump_0_test_invalid_inputs.py:19:8: E0602: Undefined variable '_CatchAllUndefinedParameters' (undefined-variable)


"""