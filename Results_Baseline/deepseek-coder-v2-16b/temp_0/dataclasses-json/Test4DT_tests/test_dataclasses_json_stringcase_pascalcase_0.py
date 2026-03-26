# Module: dataclasses_json.stringcase
import pytest
from dataclasses_json.stringcase import pascalcase

def test_pascalcase_snake_case():
    assert pascalcase("snake_case_to_camel_case") == "SnakeCaseToCamelCase"

def test_pascalcase_camel_case():
    assert pascalcase("camelCaseExample") == "CamelCaseExample"

def test_pascalcase_lowercase():
    assert pascalcase("hello world") == "HelloWorld"

def test_pascalcase_empty_string():
    assert pascalcase("") == ""
