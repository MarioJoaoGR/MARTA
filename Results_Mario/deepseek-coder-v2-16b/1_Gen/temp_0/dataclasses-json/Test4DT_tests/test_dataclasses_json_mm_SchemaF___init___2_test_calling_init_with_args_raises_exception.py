
import pytest
from dataclasses_json.mm import SchemaF

def test_calling_init_with_args_raises_exception():
    with pytest.raises(NotImplementedError):
        SchemaF()
