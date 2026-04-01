
# Assuming the module is named dataclasses_json.mm
from dataclasses_json.mm import SchemaF
import pytest

def test_schemaf_not_instantiable():
    with pytest.raises(NotImplementedError):
        SchemaF()

def test_schemaf_should_raise_exception_on_init():
    with pytest.raises(NotImplementedError):
        SchemaF().__init__()
