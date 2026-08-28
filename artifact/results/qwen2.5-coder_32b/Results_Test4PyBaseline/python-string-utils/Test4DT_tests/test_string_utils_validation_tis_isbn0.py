# Module: string_utils.validation
import pytest
from string_utils.validation import is_isbn

def test_valid_isbn_13_with_hyphens():
    assert is_isbn('978-0-312-49858-0') == True, "Valid ISBN-13 with hyphens should return True"

def test_valid_isbn_13_without_hyphens():
    assert is_isbn('9780312498580') == True, "Valid ISBN-13 without hyphens should return True"

def test_valid_isbn_10_with_hyphens():
    assert is_isbn('0-306-40615-2') == True, "Valid ISBN-10 with hyphens should return True"

def test_valid_isbn_10_without_hyphens():
    assert is_isbn('0306406152', normalize=False) == True, "Valid ISBN-10 without hyphens should return True"

def test_invalid_isbn_10_with_hyphens_when_not_normalized():
    assert is_isbn('0-306-40615-2', normalize=False) == False, "Invalid ISBN-10 with hyphens when not normalized should return False"

def test_invalid_isbn_10():
    assert is_isbn('1234567890') == False, "Invalid ISBN-10 should return False"

def test_invalid_isbn_13():
    assert is_isbn('1234567890123') == False, "Invalid ISBN-13 should return False"

def test_empty_string():
    assert is_isbn('') == False, "Empty string should return False"

def test_non_numeric_string():
    assert is_isbn('abcdefghij') == False, "Non-numeric string should return False"

def test_too_short_isbn_10():
    assert is_isbn('030640615') == False, "Too short ISBN-10 should return False"

def test_too_long_isbn_10():
    assert is_isbn('03064061523') == False, "Too long ISBN-10 should return False"

def test_too_short_isbn_13():
    assert is_isbn('978031249858') == False, "Too short ISBN-13 should return False"

def test_too_long_isbn_13():
    assert is_isbn('97803124985801') == False, "Too long ISBN-13 should return False"
