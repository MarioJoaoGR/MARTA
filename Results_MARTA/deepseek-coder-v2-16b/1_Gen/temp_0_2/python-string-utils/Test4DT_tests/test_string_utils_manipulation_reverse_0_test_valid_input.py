
import pytest
from string_utils.manipulation import reverse, InvalidInputError

def test_valid_input():
    assert reverse('hello') == 'olleh'
    with pytest.raises(InvalidInputError):
        reverse(123)
