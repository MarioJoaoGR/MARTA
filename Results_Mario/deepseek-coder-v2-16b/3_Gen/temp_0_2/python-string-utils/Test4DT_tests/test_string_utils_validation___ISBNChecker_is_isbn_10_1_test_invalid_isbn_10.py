
import pytest
from string_utils.validation import __ISBNChecker

def test_invalid_isbn_10():
    # Test an invalid ISBN-10 number
    checker = __ISBNChecker("978-0-471-60695-7")
    assert not checker.is_isbn_10()
    
    # Test another invalid ISBN-10 number with normalization disabled
    checker = __ISBNChecker("978-0-471-60695-7", normalize=False)
    assert not checker.is_isbn_10()
    
    # Test an invalid ISBN-10 number without normalization
    checker = __ISBNChecker("0471606957")
    assert not checker.is_isbn_10()
