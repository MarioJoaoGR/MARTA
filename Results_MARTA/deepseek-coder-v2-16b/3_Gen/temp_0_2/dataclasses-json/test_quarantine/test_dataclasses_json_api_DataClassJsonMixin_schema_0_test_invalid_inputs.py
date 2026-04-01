
import pytest
from my_module import MyDataClass, build_schema

class MyMixin: pass

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Attempt to call the schema function without providing a dataclass type
        build_schema(None, MyMixin)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_schema_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_0_test_invalid_inputs.py:3:0: E0401: Unable to import 'my_module' (import-error)


"""