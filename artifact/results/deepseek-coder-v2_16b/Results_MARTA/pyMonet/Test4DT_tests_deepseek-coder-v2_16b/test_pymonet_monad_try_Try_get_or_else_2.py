
import pytest
from pymonet.monad_try import Try

# Test valid input where Try is successful and has a valid value
def test_valid_input():
    try1 = Try(42, True)
    assert not try1.is_success == False
    assert try1.value == 42

# Test edge case where Try is not successful (is_success is False) and has a default value provided
def test_edge_case():
    try2 = Try("error", False)
    assert try2.is_success == False
    assert try2.get_or_else("default") == "default"

# Test method get_or_else with successful Try object
def test_get_or_else_successful():
    try1 = Try(42, True)
    assert try1.get_or_else("default") == 42

# Test method get_or_else with failed Try object
def test_get_or_else_failed():
    try2 = Try("error", False)
    assert try2.get_or_else("default") == "default"
