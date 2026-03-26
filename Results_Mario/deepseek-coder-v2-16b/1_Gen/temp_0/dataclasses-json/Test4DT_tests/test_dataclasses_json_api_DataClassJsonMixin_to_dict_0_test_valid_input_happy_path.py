
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Optional, Any
from dataclasses_json import api as dcj_api  # Corrected the import statement

class DataClassJsonMixin:
    """
        DataClassJsonMixin is an ABC that functions as a Mixin for adding JSON serialization capabilities to dataclass instances.
    
        As with other ABCs, it should not be instantiated directly.
        
        Parameters:
            self: The instance of the DataClassJsonMixin subclass that this method is called on. This parameter is automatically passed by Python and does not need to be specified when calling the method.
            encode_json (bool): A flag indicating whether to convert non-JSON compatible types to JSON format recursively within the dictionary. If set to True, certain types such as nested collections or specific dataclass instances may be encoded according to global encoder configurations. The default value is False.
        
        Returns:
            dict: A dictionary representation of the instance, potentially with encoded values and transformed keys according to user overrides or extensions.
        
        Examples:
            To convert a dataclass instance into a dictionary for JSON serialization:
            
            ```python
            from your_module import MyDataClass, DataClassJsonMixin
            
            @dataclasses.dataclass
            class MyDataClass(DataClassJsonMixin):
                name: str
                age: int
            
            data = MyDataClass(name="John Doe", age=30)
            result = data.to_dict()  # Converts the dataclass instance to a dictionary without JSON encoding.
            print(result)  # Outputs a dictionary with field names as keys and their values.
            
            encoded_data = data.to_dict(encode_json=True)  # Converts the dataclass instance to a dictionary with JSON encoding applied.
            print(encoded_data)  # Outputs a dictionary with potentially encoded values and keys.
            ```
        
        Notes:
            This method dynamically handles different types of input objects by checking if they are dataclasses, mappings, collections, or have associated encoders in the global configuration. It applies deep copying for non-dataclass, non-mapping, non-collection types to ensure that only supported structures are processed recursively. The `encode_json` flag is used to apply JSON encoding transformations on nested structures as needed.
    """
    dataclass_json_config: Optional[dict] = None
    
    def to_dict(self, encode_json=False) -> Dict[str, Any]:
        return dcj_api._asdict(self, encode_json=encode_json)

@dataclass
class MyDataClass(DataClassJsonMixin):
    name: str
    age: int

def test_valid_input_happy_path():
    data = MyDataClass(name="John Doe", age=30)
    result = data.to_dict()
    assert isinstance(result, dict)
    assert "name" in result and result["name"] == "John Doe"
    assert "age" in result and result["age"] == 30
    
    encoded_data = data.to_dict(encode_json=True)
    assert isinstance(encoded_data, dict)
    assert "name" in encoded_data and encoded_data["name"] == "John Doe"
    assert "age" in encoded_data and encoded_data["age"] == 30
