
import pytest
from dataclasses_json.mm import SchemaF  # Correctly importing from 'dataclasses_json.mm'

def test_schemaf_instantiation():
    with pytest.raises(NotImplementedError):
        SchemaF()  # Attempting to instantiate the class should raise NotImplementedError
