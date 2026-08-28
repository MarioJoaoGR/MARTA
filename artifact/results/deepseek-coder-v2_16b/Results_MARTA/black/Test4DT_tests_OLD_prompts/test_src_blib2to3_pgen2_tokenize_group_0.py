
import pytest
from blib2to3.pgen2.tokenize import group

def test_group_with_multiple_choices():
    pattern = group("apple", "banana", "cherry")
    assert pattern == "(apple|banana|cherry)"

def test_group_with_four_choices():
    pattern = group("a", "b", "c", "d")
    assert pattern == "(a|b|c|d)"

def test_group_with_single_choice():
    pattern = group("hello")
    assert pattern == "(hello)"
