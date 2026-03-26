
import pytest
from string_utils.validation import InvalidInputError

class __ISBNChecker:
    def __init__(self, input_string: str, normalize: bool = True):
        if not isinstance(input_string, str):
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
    with pytest.raises(InvalidInputError):
        checker = __ISBNChecker(9780470059029)  # Invalid input type, should raise InvalidInputError
