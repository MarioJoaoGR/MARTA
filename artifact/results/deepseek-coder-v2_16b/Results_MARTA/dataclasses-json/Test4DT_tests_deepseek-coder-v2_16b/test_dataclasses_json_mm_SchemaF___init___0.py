
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json

# Assuming MyClass is defined in a module named 'dataclasses_json.mm'
# from dataclasses_json.mm import MyClass

@dataclass
class MyClass:
    required_param1: str
    optional_param2: int = None
    optional_param3: float = None

@dataclass_json
@dataclass
class MyClassWithJson(MyClass):
    pass

# Test cases for MyClass and MyClassWithJson



def test_to_dict_method_with_json():
    my_instance = MyClassWithJson("example_value", optional_param2=42, optional_param3=3.14)
    dict_representation = my_instance.to_dict()
    assert dict_representation == {'required_param1': 'example_value', 'optional_param2': 42, 'optional_param3': 3.14}

def test_to_json_method_with_json():
    my_instance = MyClassWithJson("example_value", optional_param2=42, optional_param3=3.14)
    json_representation = my_instance.to_json()
    assert json_representation == '{"required_param1": "example_value", "optional_param2": 42, "optional_param3": 3.14}'