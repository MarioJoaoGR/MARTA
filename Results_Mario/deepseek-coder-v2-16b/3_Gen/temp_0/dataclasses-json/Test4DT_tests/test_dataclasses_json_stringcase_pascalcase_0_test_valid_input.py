
import pytest
from dataclasses_json.stringcase import pascalcase

def test_valid_input():
    assert pascalcase("hello_world") == "HelloWorld"
    assert pascalcase("camelCaseExample") == "CamelCaseExample"
    assert pascalcase("snake_case_to_camel_case") == "SnakeCaseToCamelCase"
    assert pascalcase("") == ""
