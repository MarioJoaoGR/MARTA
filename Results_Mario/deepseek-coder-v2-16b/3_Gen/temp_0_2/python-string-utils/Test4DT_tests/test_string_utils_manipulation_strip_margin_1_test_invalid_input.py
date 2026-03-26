
import pytest
from string_utils.manipulation import strip_margin, InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        strip_margin(None)
