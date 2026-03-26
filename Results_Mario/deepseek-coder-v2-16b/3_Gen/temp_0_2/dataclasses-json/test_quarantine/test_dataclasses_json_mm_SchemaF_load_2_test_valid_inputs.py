
import pytest
from dataclasses import dataclass
from dataclasses_json.mm import SchemaF

@dataclass
class ExampleData:
    key: str

def test_valid_inputs():
    schema = SchemaF()
    
    # Valid data should be returned as is
    valid_data = {'key': 'value'}
    result = schema.load(valid_data)
    assert isinstance(result, ExampleData)
    assert result.key == 'value'
    
    # Invalid data with an unknown key will raise an error unless 'unknown' parameter is set to 'ignore'
    invalid_data = {'key': 'value', 'extra_key': 'extra_value'}
    try:
        result = schema.load(invalid_data, unknown='ignore')
    except Exception as e:
        assert str(e) == "Unknown key 'extra_key' found in data"
    
    # If you expect multiple instances of the schema in your data, set many=True
    multi_instance_data = [{'key': 'value'}, {'key': 'another_value'}]
    results = schema.load(multi_instance_data, many=True)
    assert isinstance(results, list) and all(isinstance(item, ExampleData) for item in results)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF_load_2_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_2_test_valid_inputs.py:15:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_2_test_valid_inputs.py:22:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_2_test_valid_inputs.py:28:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""