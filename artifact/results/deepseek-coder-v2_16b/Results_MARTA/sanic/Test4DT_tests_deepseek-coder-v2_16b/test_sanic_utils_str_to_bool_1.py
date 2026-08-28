
import pytest
from sanic import Sanic
from sanic.response import text

# Assuming str_to_bool is defined in a module named 'sanic.utils'
def str_to_bool(val: str) -> bool:
    """Takes string and tries to turn it into bool as human would do.

    If val is in case insensitive (
        "y", "yes", "yep", "yup", "t",
        "true", "on", "enable", "enabled", "1"
    ) returns True.
    If val is in case insensitive (
        "n", "no", "f", "false", "off", "disable", "disabled", "0"
    ) returns False.
    Else Raise ValueError."""

    val = val.lower()
    if val in {
        "y",
        "yes",
        "yep",
        "yup",
        "t",
        "true",
        "on",
        "enable",
        "enabled",
        "1",
    }:
        return True
    elif val in {"n", "no", "f", "false", "off", "disable", "disabled", "0"}:
        return False
    else:
        raise ValueError(f"Invalid truth value {val}")

# Test cases for str_to_bool function
def test_str_to_bool_true():
    assert str_to_bool("Y") is True

def test_str_to_bool_false():
    assert str_to_bool("N") is False

def test_str_to_bool_invalid():
    with pytest.raises(ValueError):
        str_to_bool("maybe")
