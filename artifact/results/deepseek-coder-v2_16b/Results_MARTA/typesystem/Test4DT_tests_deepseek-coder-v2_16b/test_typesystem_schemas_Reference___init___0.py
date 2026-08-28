
import pytest
from typesystem.schemas import Reference

# Scenario 1: Test initialization with a string target
def test_init_with_string_target():
    ref = Reference("example_schema")
    assert isinstance(ref, Reference)
    assert ref._target_string == "example_schema"

# Scenario 2: Test initialization with a Schema subclass target

# Scenario 3: Test initialization with both arguments provided
def test_init_with_both_arguments():
    definitions = {"key": "value"}
    ref = Reference("example_schema", definitions=definitions)
    assert isinstance(ref, Reference)
    assert ref._target_string == "example_schema"
    assert ref.definitions == definitions