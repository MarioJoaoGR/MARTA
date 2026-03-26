
import pytest
from dataclasses_json.mm import SchemaF

def test_edge_cases():
    schema = SchemaF()
    obj = {"key": "value"}
    json_str = schema.dumps(obj)
    assert isinstance(json_str, str), f"Expected a JSON string but got {type(json_str)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF_dumps_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_0_test_edge_cases.py:8:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""