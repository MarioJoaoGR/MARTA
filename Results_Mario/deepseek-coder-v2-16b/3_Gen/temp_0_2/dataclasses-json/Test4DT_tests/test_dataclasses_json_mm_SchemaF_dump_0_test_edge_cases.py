
from dataclasses_json.mm import SchemaF  # Correcting the import path as per the error message
import pytest

def test_schemaf_instantiation():
    with pytest.raises(NotImplementedError):
        SchemaF()
