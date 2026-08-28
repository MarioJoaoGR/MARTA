
import pytest
import re
from ansible.module_utils.common.dict_transformations import _camel_to_snake

def test_camel_to_snake_basic():
    name = "CamelCaseName"
    expected_output = "camel_case_name"
    assert _camel_to_snake(name) == expected_output


def test_camel_to_snake_reversible_without_abbreviation():
    name = "CamelCaseName"
    expected_output = "camel_case_name"
    assert _camel_to_snake(name, reversible=True) == expected_output