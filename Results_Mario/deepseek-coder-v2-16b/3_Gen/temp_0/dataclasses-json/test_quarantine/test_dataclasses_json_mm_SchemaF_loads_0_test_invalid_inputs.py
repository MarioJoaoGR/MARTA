
import pytest
from dataclasses_json import SchemaF  # Assuming this is the correct module for SchemaF

def test_schemaf_should_not_be_instantiated():
    with pytest.raises(NotImplementedError):
        SchemaF()

def test_schemaf_should_not_be_inherited():
    class SubSchemaF(SchemaF):
        pass
    
    with pytest.raises(TypeError):
        SubSchemaF()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF_loads_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_loads_0_test_invalid_inputs.py:3:0: E0611: No name 'SchemaF' in module 'dataclasses_json' (no-name-in-module)


"""