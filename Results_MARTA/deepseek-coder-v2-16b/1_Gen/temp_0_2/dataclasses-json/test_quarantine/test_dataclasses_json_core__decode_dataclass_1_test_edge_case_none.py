
import pytest
from dataclasses import dataclass, fields
from typing import Optional
from dataclasses_json.core import _decode_dataclass

@dataclass
class TestDataclass:
    field1: Optional[str] = None

def test_edge_case_none():
    # Define the JSON-compatible dictionary or string to be deserialized
    kvs = {"field1": None}
    
    # Call the function with the dataclass type, the data, and infer_missing set to True
    result = _decode_dataclass(TestDataclass, kvs, True)
    
    # Assert that the result is an instance of TestDataclass with field1 set to None
    assert isinstance(result, TestDataclass)
    assert result.field1 is None
