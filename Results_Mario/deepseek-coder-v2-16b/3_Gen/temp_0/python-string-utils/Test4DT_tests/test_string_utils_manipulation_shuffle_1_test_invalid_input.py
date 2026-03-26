
import pytest
from string_utils.manipulation import shuffle, InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        shuffle(12345)
