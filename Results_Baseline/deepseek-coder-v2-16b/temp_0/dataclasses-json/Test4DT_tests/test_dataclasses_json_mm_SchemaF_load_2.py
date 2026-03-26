# Module: dataclasses_json.mm
# test_schemaf.py
import pytest
from dataclasses_json.mm import SchemaF

def test_schemaf_instantiation():
    with pytest.raises(NotImplementedError):
        SchemaF()
