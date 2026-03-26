
import pytest
from dataclasses_json import mm  # Assuming 'mm' is the module where _ExtendedEncoder might be defined

@pytest.fixture
def schema_instance():
    class MySchema(mm.Schema):
        pass
    return MySchema()

def test_invalid_input_missing_cls_arg(schema_instance):
    with pytest.raises(TypeError) as excinfo:
        schema_instance.dumps()
    assert "missing 1 required positional argument: 'obj'" in str(excinfo.value)
