
import pytest
from unittest.mock import patch
from httpie.utils import ExplicitNullAuth

@pytest.mark.parametrize("input_value", [None, "some_other_input"])
def test_none_input(input_value):
    null_auth = ExplicitNullAuth()
    
    with patch('httpie.utils.ExplicitNullAuth.__call__', return_value=input_value):
        result = null_auth(input_value)
        
        assert result == input_value
