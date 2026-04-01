
import pytest
from dataclasses_json.mm import SchemaF

# Assuming Example is a dataclass defined elsewhere
from your_module import Example  # Replace 'your_module' with the actual module where Example is defined

def test_valid_input():
    # Create an instance of Example
    example = Example(field1="value1", field2=123)
    
    # Convert to JSON string using SchemaF.dumps
    json_str = SchemaF.dumps(example)
    
    # Add assertions to check if the conversion is valid
    assert isinstance(json_str, str)
    # You can add more assertions based on what you expect from a valid input conversion

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF_dumps_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_0_test_valid_input.py:6:0: E0401: Unable to import 'your_module' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_0_test_valid_input.py:13:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_dumps_0_test_valid_input.py:13:15: E1120: No value for argument 'obj' in unbound method call (no-value-for-parameter)


"""