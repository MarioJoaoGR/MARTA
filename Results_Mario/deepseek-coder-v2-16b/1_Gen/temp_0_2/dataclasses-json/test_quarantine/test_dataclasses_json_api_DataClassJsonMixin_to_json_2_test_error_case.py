
import pytest
from dataclasses import dataclass
from typing import Optional, Union, Tuple, Callable
import json
from dataclasses_json.api import DataClassJsonMixin

# Define a sample dataclass for testing
@dataclass
class SampleDataClass(DataClassJsonMixin):
    name: str
    age: int

def test_to_json_method():
    # Create an instance of the dataclass
    obj = SampleDataClass(name='John Doe', age=30)
    
    # Call the to_json method
    json_str = obj.to_json()
    
    # Check if the output is a JSON string
    assert isinstance(json_str, str), "Expected a JSON string"
    
    # Parse the JSON string and check its content
    parsed_data = json.loads(json_str)
    assert parsed_data['name'] == 'John Doe'
    assert parsed_data['age'] == 30

# Run the test
if __name__ == "__main__":
    pytest.main()
