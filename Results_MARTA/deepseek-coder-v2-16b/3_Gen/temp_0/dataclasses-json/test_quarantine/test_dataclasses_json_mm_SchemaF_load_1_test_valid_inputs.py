
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
    encoded_data = {"field1": "example", "field2": 42}
    result = schema.load(encoded_data)
    assert isinstance(result, DataClassExample)
    assert result.field1 == "example"
    assert result.field2 == 42
    
    # Test with valid data for multiple items
    multi_encoded_data = [{"field1": "example", "field2": 42}, {"field1": "test", "field2": 100}]
    many_result = schema.load(multi_encoded_data, many=True)
    assert isinstance(many_result, list)
    assert len(many_result) == 2
    assert all(isinstance(item, DataClassExample) for item in many_result)
    assert many_result[0].field1 == "example" and many_result[0].field2 == 42
    assert many_result[1].field1 == "test" and many_result[1].field2 == 100
    
    # Test with partial data (should raise an error)
    partial_data = {"field1": "example"}
    with pytest.raises(Exception):
        schema.load(partial_data, partial=False)
    
    # Test with unknown field (should ignore the unknown field)
    unknown_data = {"field1": "example", "field2": 42, "unknown_field": "extra"}
    result_with_unknown = schema.load(unknown_data, unknown="ignore")
    assert isinstance(result_with_unknown, DataClassExample)
    assert result_with_unknown.field1 == "example"
    assert result_with_unknown.field2 == 42

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF_load_1_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_1_test_valid_inputs.py:16:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_1_test_valid_inputs.py:23:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_1_test_valid_inputs.py:37:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""