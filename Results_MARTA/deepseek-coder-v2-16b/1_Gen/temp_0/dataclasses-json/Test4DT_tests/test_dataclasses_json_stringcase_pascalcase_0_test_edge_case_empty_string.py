
import pytest
from dataclasses_json import stringcase

def test_pascalcase_empty_string():
    assert stringcase.pascalcase("") == ''
