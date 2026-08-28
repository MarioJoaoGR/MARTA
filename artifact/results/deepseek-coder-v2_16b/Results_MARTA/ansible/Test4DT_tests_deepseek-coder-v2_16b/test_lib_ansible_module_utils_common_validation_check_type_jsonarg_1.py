
import pytest
from ansible.module_utils.common.validation import check_type_jsonarg
import json


def test_dictionary():
    value = {"key": "value"}
    result = check_type_jsonarg(value)
    assert result == json.dumps(value, ensure_ascii=False)

def test_string():
    value = "   some text with spaces   "
    result = check_type_jsonarg(value)
    assert result == value.strip()

def test_list():
    value = ["key", "value"]
    result = check_type_jsonarg(value)
    assert result == json.dumps(value, ensure_ascii=False)