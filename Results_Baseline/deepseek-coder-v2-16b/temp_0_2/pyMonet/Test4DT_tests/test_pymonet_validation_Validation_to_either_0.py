# Module: pymonet.validation
import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right

# Successful Scenario
def test_successful_creation():
    val_success = Validation(10, [])
    assert val_success.value == 10
    assert val_success.errors == []

# Failed Scenario
def test_failed_creation():
    val_failure = Validation(None, ["Error message"])
    assert val_failure.value is None
    assert val_failure.errors == ["Error message"]

# Using the `is_success` Method
def test_is_success_true():
    val_success = Validation(10, [])
    assert val_success.is_success() is True

def test_is_success_false():
    val_failure = Validation(None, ["Error message"])
    assert val_failure.is_success() is False

# Using the `to_either` Method
def test_to_either_success():
    val_success = Validation(10, [])
    either_success = val_success.to_either()
    assert isinstance(either_success, Right)
    assert either_success.value == 10

def test_to_either_failure():
    val_failure = Validation(None, ["Error message"])
    either_failure = val_failure.to_either()
    assert isinstance(either_failure, Left)
    assert either_failure.value == ["Error message"]
