# Module: dataclasses_json.mm
# test_schemaf.py
import pytest
from dataclasses_json.mm import SchemaF

def test_schemaf_instantiation():
    with pytest.raises(NotImplementedError):
        schema_f = SchemaF()

if __name__ == "__main__":
    pytest.main()
