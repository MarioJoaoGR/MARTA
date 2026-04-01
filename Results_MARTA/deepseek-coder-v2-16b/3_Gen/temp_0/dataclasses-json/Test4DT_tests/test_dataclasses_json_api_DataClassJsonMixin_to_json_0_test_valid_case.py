
from dataclasses_json.api import DataClassJsonMixin
import pytest
import json
from typing import Optional, Union, Tuple, Callable
import dataclasses

@pytest.fixture
def valid_data():
    @dataclasses.dataclass
    class MyDataClass(DataClassJsonMixin):
        name: str
        age: int
    
    return MyDataClass(name="John Doe", age=30)

def test_to_json_valid_case(valid_data):
    json_string = valid_data.to_json()
    assert isinstance(json_string, str), "Expected a JSON string"
    
    # Deserialize the JSON string to verify its content
    data_dict = json.loads(json_string)
    assert data_dict['name'] == 'John Doe', "Name does not match expected value"
    assert data_dict['age'] == 30, "Age does not match expected value"
