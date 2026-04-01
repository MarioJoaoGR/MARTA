
def is_unicode_scalar_value(codepoint: int) -> bool:
    return (0 <= codepoint <= 55295) or (57344 <= codepoint <= 1114111)

def test_valid_case_low_boundary():
    # Test the lowest valid Unicode scalar value boundary
    assert is_unicode_scalar_value(0) == True

def test_valid_case_high_boundary():
    # Test the highest valid Unicode scalar value boundary
    assert is_unicode_scalar_value(55295) == True

def test_invalid_case_low_boundary():
    # Test the lowest invalid Unicode scalar value boundary
    assert is_unicode_scalar_value(55296) == False

def test_invalid_case_high_boundary():
    # Test the highest invalid Unicode scalar value boundary
    assert is_unicode_scalar_value(1114111) == True
