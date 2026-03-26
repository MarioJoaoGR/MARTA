
import pytest
from dataclasses_json.api import DataClassJsonMixin
import json
from typing import Optional, Union, Tuple, Callable
import dataclasses

# Mocking _ExtendedEncoder for the test case
class MockEncoder(json.JSONEncoder):
    pass

@pytest.fixture
def data_instance():
    @dataclasses.dataclass
    class MyDataClass(DataClassJsonMixin):
        name: str
        age: int
    
    return MyDataClass(name="John Doe", age=30)

def test_to_json(data_instance):
    json_string = data_instance.to_json()
    assert isinstance(json_string, str), "Expected a JSON string"
