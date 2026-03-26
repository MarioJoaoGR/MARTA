
import pytest
from dataclasses_json.api import DataClassJsonMixin
import dataclasses

@dataclasses.dataclass
class MyDataClass(DataClassJsonMixin):
    name: str
    age: int

def test_edge_case_none():
    data = MyDataClass(name="John Doe", age=30)
    result = data.to_dict()  # Converts the dataclass instance to a dictionary without JSON encoding.
    assert isinstance(result, dict), "The result should be a dictionary"
