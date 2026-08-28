
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json

# Define a simple data class for testing
@dataclass_json
@dataclass
class MyClass:
    param1: int
    param2: str

# Define the schema mock
class SchemaMock:
    def dump(self, obj, *, many=None):
        if isinstance(obj, list):
            return [{"param1": item.param1, "param2": item.param2} for item in obj]
        elif isinstance(obj, MyClass):
            return {"param1": obj.param1, "param2": obj.param2}
        else:
            raise ValueError("Invalid input")

# Test valid single object serialization
def test_valid_single_object():
    my_instance = MyClass(param1=1, param2='example')
    schema_mock = SchemaMock()
    result = schema_mock.dump(obj=my_instance, many=False)
    assert result == {"param1": 1, "param2": 'example'}

# Test invalid input handling
def test_invalid_input():
    schema_mock = SchemaMock()
    with pytest.raises(ValueError):
        schema_mock.dump(obj=None, many=False)
