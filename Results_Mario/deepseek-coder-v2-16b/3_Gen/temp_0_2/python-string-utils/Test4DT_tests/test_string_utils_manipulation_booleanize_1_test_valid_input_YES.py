
import pytest
from string_utils.manipulation import booleanize

def test_valid_input_YES():
    assert booleanize('YES') == True
