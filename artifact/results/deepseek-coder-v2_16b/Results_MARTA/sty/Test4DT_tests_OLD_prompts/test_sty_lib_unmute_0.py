
import pytest
from unittest.mock import patch
from sty.lib import Register, unmute



def test_unmute_invalid_object():
    invalid_obj = "Not a Register"
    with pytest.raises(ValueError, match="The unmute\(\) method can only be used with objects that inherit from the 'Register class'."):
        unmute(invalid_obj)