# Module: pymonet.monad_try
# test_monad_try.py
import pytest
from pymonet.monad_try import Try

# Test initialization of a successful Try instance
def test_successful_init():
    try_instance = Try(42, True)
    assert try_instance.value == 42
    assert try_instance.is_success is True

# Test initialization of a failed Try instance
def test_failed_init():
    try_failure = Try("example", False)
    assert try_failure.value == "example"
    assert try_failure.is_success is False

# Test get_or_else method with successful Try instance
def test_get_or_else_successful():
    try_instance = Try(42, True)
    result = try_instance.get_or_else(0)
    assert result == 42

# Test get_or_else method with failed Try instance
def test_get_or_else_failed():
    try_failure = Try("example", False)
    result = try_failure.get_or_else("default")
    assert result == "default"

# Test get_or_else method with a different default value for failed Try instance
def test_get_or_else_with_different_default():
    try_failure = Try("example", False)
    result = try_failure.get_or_else(None)
    assert result is None

# Test get_or_else method with a non-string default value for failed Try instance
def test_get_or_else_with_non_string_default():
    try_failure = Try("example", False)
    result = try_failure.get_or_else(123)
    assert result == 123
