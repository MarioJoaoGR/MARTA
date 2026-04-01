
import pytest
from dataclasses_json import SchemaF

def test_schemaf_loads():
    with pytest.raises(NotImplementedError):
        schema_instance = SchemaF()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF_loads_3_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_loads_3_test_edge_case.py:3:0: E0611: No name 'SchemaF' in module 'dataclasses_json' (no-name-in-module)


"""