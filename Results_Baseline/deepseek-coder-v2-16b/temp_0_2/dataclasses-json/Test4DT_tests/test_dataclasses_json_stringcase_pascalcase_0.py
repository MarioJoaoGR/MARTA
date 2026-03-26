# Module: dataclasses_json.stringcase
import pytest
from dataclasses_json.stringcase import pascalcase

def test_pascalcase_simple_sentence():
    assert pascalcase("hello world") == 'HelloWorld'

def test_pascalcase_camel_case_phrase():
    assert pascalcase("CamelCase is popular") == 'CamelCaseIsPopular'

def test_pascalcase_underscored_string():
    assert pascalcase("snake_case_to_camel_case") == 'SnakeCaseToCamelCase'

def test_pascalcase_hyphenated_string():
    assert pascalcase("kebab-case-to-camel-case") == 'KebabCaseToCamelCase'

def test_pascalcase_empty_string():
    assert pascalcase("") == ''

def test_pascalcase_single_letter():
    assert pascalcase("a") == 'A'

def test_pascalcase_already_pascal_case():
    assert pascalcase("PascalCaseIsCorrect") == 'PascalCaseIsCorrect'
