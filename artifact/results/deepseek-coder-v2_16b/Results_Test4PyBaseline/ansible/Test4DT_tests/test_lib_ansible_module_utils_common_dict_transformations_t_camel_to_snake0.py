
import pytest
import re
from ansible.module_utils.common.dict_transformations import _camel_to_snake

# Test cases for _camel_to_snake function

def test_camel_to_snake_basic():
    assert _camel_to_snake("CamelCaseName") == "camel_case_name"

def test_camel_to_snake_reversible():
    assert _camel_to_snake("TargetGroupARNs", reversible=True) == "target_group_ar_ns"

def test_camel_to_snake_non_reversible():
    assert _camel_to_snake("AnotherCamelCase", reversible=False) == "another_camel_case"

def test_camel_to_snake_with_numbers():
    assert _camel_to_snake("CamelCaseName123") == "camel_case_name123"

def test_camel_to_snake_all_caps():
    assert _camel_to_snake("ALLCAPSINTHENAME") == "allcapsinthename"

def test_camel_to_snake_empty_string():
    assert _camel_to_snake("") == ""

def test_camel_to_snake_single_letter():
    assert _camel_to_snake("A") == "a"

def test_camel_to_snake_no_change():
    assert _camel_to_snake("already_snake_case") == "already_snake_case"

def test_camel_to_snake_reversible_with_numbers():
    assert _camel_to_snake("TargetGroupARNs123", reversible=True) == "target_group_ar_ns123"
