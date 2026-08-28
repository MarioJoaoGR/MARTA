
import pytest
from ansible.plugins.filter import core as filter_core

# Assuming to_bool is defined in the same module or can be imported correctly
to_bool = filter_core.to_bool


def test_to_bool_with_true_boolean():
    assert to_bool(True) is True

def test_to_bool_with_false_boolean():
    assert to_bool(False) is False

def test_to_bool_with_truthy_string():
    assert to_bool('Yes') is True

def test_to_bool_with_falsy_string():
    assert to_bool('OFF') is False

def test_to_bool_with_truthy_integer():
    assert to_bool(1) is True

def test_to_bool_with_falsy_integer():
    assert to_bool(0) is False

def test_to_bool_with_truthy_string_case_insensitive():
    assert to_bool('true') is True

def test_to_bool_with_falsy_string_case_insensitive():
    assert to_bool('false') is False