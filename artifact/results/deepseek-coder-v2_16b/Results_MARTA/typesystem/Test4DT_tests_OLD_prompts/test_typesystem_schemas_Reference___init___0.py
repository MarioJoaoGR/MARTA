
import pytest
from typesystem.schemas import Schema, Reference

# Scenario 1: Creating a Reference object with a string target
def test_reference_with_string_target():
    ref = Reference("example_schema")
    assert isinstance(ref.to, str)
    assert ref._target_string == "example_schema"

# Scenario 2: Creating a Reference object with a Schema subclass target

# Scenario 3: Creating a Reference object with both arguments provided
def test_reference_with_both_arguments():
    definitions = {"key": "value"}
    ref = Reference("example_schema", definitions=definitions)
    assert isinstance(ref.to, str)
    assert ref._target_string == "example_schema"
    assert ref.definitions == definitions