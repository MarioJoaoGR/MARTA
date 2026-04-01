
import pytest
from dataclasses_json import SchemaF

def test_schemaf_loads():
    # Test the loads method of SchemaF with valid input
    json_data = '[{"name": "John Doe", "age": 30}, {"name": "Jane Doe", "age": 25}]'
    persons = SchemaF.loads(json_data, many=True)
    assert len(persons) == 2
    assert all(isinstance(person, dict) for person in persons)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF_loads_2_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_loads_2_test_valid_input.py:3:0: E0611: No name 'SchemaF' in module 'dataclasses_json' (no-name-in-module)


"""