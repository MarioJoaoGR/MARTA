
import pytest
from string_utils.validation import InvalidInputError

class __ISBNChecker:
    """
    A class for checking and normalizing ISBN numbers.

    The `__ISBNChecker` class is designed to validate and optionally normalize ISBN-10 and ISBN-13 numbers by removing hyphens. It accepts an input string representing the potential ISBN number, along with a boolean flag to control normalization.

    Parameters:
        input_string (str): A string that represents the ISBN number. This should be either an ISBN-10 or ISBN-13 number.
        normalize (bool, optional): If set to `True` (default), hyphens will be removed from the input string before processing. If set to `False`, the input string is used as provided without modification.

    Raises:
        InvalidInputError: If the provided `input_string` is not a string, this error will be raised.

    Returns:
        None directly. However, the class instance stores the normalized or unmodified ISBN number in the attribute `self.input_string`.

    Example Usage:
        >>> checker = __ISBNChecker("978-0-13-235088-4")
        >>> print(checker.input_string)  # Output: "9780132350884"
        
        >>> checker = __ISBNChecker("0-13-235088-4", normalize=False)
        >>> print(checker.input_string)  # Output: "0132350884"
    """
    def __init__(self, input_string: str, normalize: bool = True):
        if not isinstance(input_string, str):
            raise InvalidInputError(input_string)

        self.input_string = input_string.replace('-', '') if normalize else input_string

    def is_isbn_13(self) -> bool:
        if len(self.input_string) == 13:
            product = 0

            try:
                for index, digit in enumerate(self.input_string):
                    weight = 1 if (index % 2 == 0) else 3
                    product += int(digit) * weight

                return product % 10 == 0

            except ValueError:
                pass

        return False

def test_valid_isbn_13():
    checker = __ISBNChecker("9780470059029")
    assert checker.is_isbn_13() == True

    checker = __ISBNChecker("978-0-470-05902-9", normalize=False)
    assert checker.is_isbn_13() == False

    with pytest.raises(InvalidInputError):
        checker = __ISBNChecker(123456)
