
import re
from string_utils.validation import is_string

class InvalidInputError(Exception):
    pass

class __ISBNChecker:
    def __init__(self, input_string: str, normalize: bool = True):
        if not is_string(input_string):
            raise InvalidInputError(input_string)

        self.input_string = input_string.replace('-', '') if normalize else input_string

    def is_isbn_10(self) -> bool:
        if len(self.input_string) == 10:
            product = 0

            try:
                for index, digit in enumerate(self.input_string):
                    product += int(digit) * (index + 1)

                return product % 11 == 0

            except ValueError:
                pass

        return False

def test_invalid_isbn_10():
    # Test with invalid ISBN-10 numbers
    checker = __ISBNChecker("978-0-471-60695-7")
    assert not checker.is_isbn_10(), "Expected False for invalid ISBN-10 number"

    checker = __ISBNChecker("978-0-471-60695-7", normalize=False)
    assert not checker.is_isbn_10(), "Expected False for invalid ISBN-10 number with normalization disabled"

    # Test with a string that is too short to be an ISBN-10
    checker = __ISBNChecker("12345")
    assert not checker.is_isbn_10(), "Expected False for too short a string"

    # Test with a non-numeric character in the ISBN-10 number
    checker = __ISBNChecker("978-0-471-60695-a")
    assert not checker.is_isbn_10(), "Expected False for invalid character in ISBN-10 number"

    # Test with a string that contains only hyphens
    checker = __ISBNChecker("---------")
    assert not checker.is_isbn_10(), "Expected False for all hyphens"
