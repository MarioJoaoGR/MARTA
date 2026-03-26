
# Module: isort._vendored.tomli._parser
import pytest
from isort._vendored.tomli._parser import key_value_rule
from isort._vendored.tomli._shared_types import Output, Pos, Key, ParseFloat, Flags, suffixed_err, NestedDict

# Example 1: Basic Usage
def test_key_value_rule_basic():
    src = "name=John age=30"
    pos = 0
    out = Output(data=NestedDict(), flags=Flags())
    header = ("user",)
    parse_float = float

    result = key_value_rule(src, pos, out, header, parse_float)
    assert result == len("name=John age=30")  # Updated position after parsing the key-value pair

# Example 2: Handling Different Key and Value Types
def test_key_value_rule_different_types():
    src = "name='John Doe' age=30.5"
    pos = 0
    out = Output(data=NestedDict(), flags=Flags())
    header = ("user",)
    parse_float = float

    result = key_value_rule(src, pos, out, header, parse_float)
    assert result == len("name='John Doe' age=30.5")  # Updated position after parsing the key-value pair

# Example 3: Handling Errors in Key-Value Parsing
def test_key_value_rule_error():
    src = "name=John age"  # Missing equal sign after 'age'
    pos = 0
    out = Output(data=NestedDict(), flags=Flags())
    header = ("user",)
    parse_float = float

    with pytest.raises(suffixed_err):
        key_value_rule(src, pos, out, header, parse_float)

# Example 4: Handling Immutable Namespace Mutation
def test_key_value_rule_immutable_mutation():
    src = "name=John age=30"
    pos = 0
    out = Output(data=NestedDict(), flags=Flags())
    header = ("user",)
    parse_float = float

    # Attempting to mutate an immutable namespace
    with pytest.raises(suffixed_err):
        key_value_rule(src, pos, out, header, parse_float)

# Example 5: Handling Value Overwrite
def test_key_value_rule_overwrite():
    src = "name=John age=30"
    pos = 0
    out = Output(data=NestedDict(), flags=Flags())
    header = ("user",)
    parse_float = float

    # Attempting to overwrite a value in an immutable namespace
    with pytest.raises(suffixed_err):
        key_value_rule(src, pos, out, header, parse_float)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_key_value_rule_0
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0.py:5:0: E0401: Unable to import 'isort._vendored.tomli._shared_types' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0.py:5:0: E0611: No name '_shared_types' in module 'isort._vendored.tomli' (no-name-in-module)


"""