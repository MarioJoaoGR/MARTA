
import re
import pytest
from string_utils.manipulation import strip_html, InvalidInputError

def test_invalid_input():
    with pytest.raises(TypeError):
        strip_html(123)  # Should raise TypeError because input is not a string
