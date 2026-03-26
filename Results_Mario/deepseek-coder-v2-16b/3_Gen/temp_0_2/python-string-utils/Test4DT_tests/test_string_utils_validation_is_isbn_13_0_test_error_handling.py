
import pytest
from string_utils.validation import is_isbn_13

def test_error_handling():
    # Test case where input is not a string
    with pytest.raises(TypeError):
        is_isbn_13(12345)  # This should raise a TypeError

    # Test case where input length is not 13 (even if normalized or not)
    assert not is_isbn_13('978031249858')  # Should return False because length is incorrect
    assert not is_isbn_13('978-031249858', normalize=False)  # Should return False because length is incorrect

    # Test case where input contains invalid characters (non-digit characters)
    assert not is_isbn_13('978-031249858a')  # Should return False because of invalid character 'a'
    assert not is_isbn_13('978031249858a', normalize=False)  # Should return False because of invalid character 'a'
