
import pytest
from string_utils.manipulation import reverse
from string_utils.errors import InvalidInputError

def test_valid_input():
    assert reverse('hello') == 'olleh'
    assert reverse('world') == 'dlrow'
    with pytest.raises(InvalidInputError):
        reverse(123)  # Should raise InvalidInputError since 123 is not a string
