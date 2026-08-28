
import pytest
from ansible.utils.color import parsecolor, C

# Test cases for named colors
def test_parsecolor_named_colors():
    assert parsecolor('color256') == '38;5;256'