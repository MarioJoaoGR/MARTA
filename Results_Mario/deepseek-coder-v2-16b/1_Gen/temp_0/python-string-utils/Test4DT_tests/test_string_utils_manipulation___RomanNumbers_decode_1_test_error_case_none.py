
import pytest
from string_utils.manipulation import __RomanNumbers  # Assuming this is in a different module

def test_error_case_none():
    with pytest.raises(ValueError):
        result = __RomanNumbers().decode(None)
