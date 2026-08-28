
# Module: pymonet.monad_try
import pytest
from pymonet.monad_try import Try

# Test initialization of successful Try instance
def test_successful_init():
    try_instance = Try(42, True)
    assert try_instance.value == 42
    assert try_instance.is_success is True

# Test initialization of failed Try instance
def test_failed_init():
    try_instance = Try("error", False)
    assert try_instance.value == "error"
    assert try_instance.is_success is False

# Test get method for successful Try instance
def test_get_successful():
    try_instance = Try(42, True)