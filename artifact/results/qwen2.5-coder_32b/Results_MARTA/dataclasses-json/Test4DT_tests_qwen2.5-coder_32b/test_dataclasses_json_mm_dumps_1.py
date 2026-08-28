
import pytest
from dataclasses import dataclass
from dataclasses_json.mm import SchemaF, _ExtendedEncoder

@dataclass
class TestDataClass(SchemaF):
    name: str
    age: int
    hobbies: list






def test_invalid_inputs_keyword_argument_type():
    """Test that the dumps method raises a TypeError with invalid keyword argument types."""
    data_instance = TestDataClass(name="Bob", age=40, hobbies=["swimming"])
    with pytest.raises(TypeError):
        data_instance.dumps(indent="four")  # Passing a string instead of an integer for indent