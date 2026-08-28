
import pytest
from dataclasses_json.mm import SchemaF

def test_instantiation_with_no_args_raises_notimplementederror():
    with pytest.raises(NotImplementedError):
        SchemaF()

