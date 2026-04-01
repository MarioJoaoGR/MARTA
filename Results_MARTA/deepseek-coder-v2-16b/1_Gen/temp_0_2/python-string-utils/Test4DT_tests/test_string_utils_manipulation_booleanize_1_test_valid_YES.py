
import pytest
from string_utils.manipulation import booleanize, InvalidInputError

def test_valid_YES():
    assert booleanize('YES') == True
