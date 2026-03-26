
from dataclasses_json import Schema, _ExtendedEncoder
import pytest

@pytest.fixture
def schema_instance():
    class PersonSchema(Schema):
        pass
    return PersonSchema()

def test_invalid_input_missing_cls_arg(schema_instance):
    with pytest.raises(TypeError) as excinfo:
        schema_instance.dumps()
    assert "missing 1 required positional argument: 'obj'" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_dumps_1_test_invalid_input_missing_cls_arg
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_1_test_invalid_input_missing_cls_arg.py:2:0: E0611: No name 'Schema' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_1_test_invalid_input_missing_cls_arg.py:2:0: E0611: No name '_ExtendedEncoder' in module 'dataclasses_json' (no-name-in-module)

"""