# Module: string_utils.validation
import pytest
from string_utils.validation import is_isbn_10

def test_valid_isbn_10_without_hyphens():
    assert is_isbn_10('1506715214') == True, "Valid ISBN-10 without hyphens should return True"

def test_valid_isbn_10_with_hyphens_default_behavior():
    assert is_isbn_10('150-6715214') == True, "Valid ISBN-10 with hyphens should return True when normalize=True (default)"

def test_valid_isbn_10_with_hyphens_strict_validation():
    assert is_isbn_10('150-6715214', normalize=False) == False, "Valid ISBN-10 with hyphens should return False when normalize=False"

def test_invalid_isbn_10_checksum():
    assert is_isbn_10('123456789X') == False, "Invalid ISBN-10 due to incorrect checksum should return False"

def test_invalid_isbn_10_too_short():
    assert is_isbn_10('123456789') == False, "ISBN-10 that is too short should return False"

def test_invalid_isbn_10_too_long():
    assert is_isbn_10('12345678901') == False, "ISBN-10 that is too long should return False"

def test_invalid_isbn_10_with_non_digit_characters():
    assert is_isbn_10('123-456A89X', normalize=False) == False, "ISBN-10 with non-digit characters (excluding hyphen) and strict validation should return False"

def test_valid_isbn_10_with_x_as_check_digit():
    assert is_isbn_10('0306406152') == True, "Valid ISBN-10 with 'X' as check digit should return True"

def test_invalid_isbn_10_with_x_in_wrong_position():
    assert is_isbn_10('03064061X2') == False, "ISBN-10 with 'X' in the wrong position should return False"
