
import pytest
from dataclasses import dataclass
from dataclasses_json.mm import SchemaF

@dataclass
class DataClassExample:
    field1: str
    field2: int

def test_valid_inputs():
    schema = SchemaF()
    
    # Test with valid data for a single item
    encoded_data = {"field1": "example", "field2": 1}
    result = schema.load(encoded_data)
    assert isinstance(result, DataClassExample)
    assert result.field1 == "example"
    assert result.field2 == 1
    
    # Test with valid data for multiple items
    multi_encoded_data = [{"field1": "example", "field2": 1}, {"field1": "test", "field2": 2}]
    results = schema.load(multi_encoded_data, many=True)
    assert isinstance(results, list)
    assert len(results) == 2
    assert all(isinstance(item, DataClassExample) for item in results)
    assert results[0].field1 == "example" and results[0].field2 == 1
    assert results[1].field1 == "test" and results[1].field2 == 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF_load_2_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_2_test_valid_inputs.py:16:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_2_test_valid_inputs.py:23:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""