
import pytest
from dataclasses import dataclass
from typing import List, Dict, Any

# Hypothetical User data class for testing
@dataclass
class SchemaF:
    name: str
    age: int
    tags: List[str]
    metadata: Dict[str, Any]

def test_schemaf():
    # Create an instance of SchemaF
    schema = SchemaF(name="John Doe", age=30, tags=["tag1", "tag2"], metadata={"key": "value"})
    
    # Assert that the created instance has the correct properties
    assert schema.name == "John Doe"
    assert schema.age == 30
    assert schema.tags == ["tag1", "tag2"]
    assert schema.metadata == {"key": "value"}
