
import pytest
from typesystem.schemas import Reference, Schema

# Assuming 'my_module' contains the definition of ExampleSchema and UserSchema
# from my_module import ExampleSchema, UserSchema

def test_valid_input_string_target():
    with pytest.raises(ModuleNotFoundError):
        from my_module import ExampleSchema  # This will fail as 'my_module' is not defined

def test_valid_input_class_target():
    with pytest.raises(ModuleNotFoundError):
        from my_module import ExampleSchema  # This will fail as 'my_module' is not defined

def test_invalid_input_null():
    ref = Reference('example_schema')  # Assuming this works if the module were imported correctly
    assert ref.to == 'example_schema'
