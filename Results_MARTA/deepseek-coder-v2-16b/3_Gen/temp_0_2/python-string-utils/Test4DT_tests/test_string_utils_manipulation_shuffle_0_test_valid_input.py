
import pytest
from string_utils.manipulation import shuffle, InvalidInputError
import random

def is_string(value):
    return isinstance(value, str)

@pytest.mark.parametrize("input_string", [
    'hello world',
    '12345',
    '',
    'a',
    'abcde'
])
def test_valid_input(input_string):
    if not is_string(input_string):
        with pytest.raises(InvalidInputError) as excinfo:
            shuffle(input_string)
        assert str(excinfo.value) == f"Expected type 'str', but got '{type(input_string).__name__}'"
    else:
        shuffled = shuffle(input_string)
        assert len(shuffled) == len(input_string)
        assert set(shuffled) == set(input_string)
