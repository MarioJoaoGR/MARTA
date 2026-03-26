
import pytest
from typing import List, Dict

# Assuming the classes A and TEncoded are defined elsewhere in the codebase
class A: pass
class TEncoded: pass

# Mock SchemaF class with necessary methods
class SchemaF:
    def dump(self, obj: List[A], many: bool = False) -> List[TEncoded]:  # type: ignore
        if not isinstance(obj, list):
            raise ValueError("obj must be a list")
        if not isinstance(many, bool):
            raise ValueError("many must be a boolean")
        return [TEncoded() for _ in obj]

# Test invalid inputs
def test_invalid_inputs():
    schema = SchemaF()
    objs = 'not a list'
    many = 'not a bool'
    
    with pytest.raises(ValueError):
        encoded_objs = schema.dump(objs, many)
