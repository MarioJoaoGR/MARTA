
import pytest
from unittest.mock import Mock
from superstring.superstring import SuperStringBase, SuperStringLower

def test_valid_input():
    base_string = Mock(spec=SuperStringBase)
    base_string.length.return_value = 13
    lower_string = SuperStringLower(base_string)
    
    assert lower_string.length() == 13
