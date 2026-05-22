
import pytest
from httpie.plugins.builtin import HTTPBearerAuth
from unittest.mock import patch

def test_invalid_input():
    with pytest.raises(TypeError):
        with patch('httpie.plugins.builtin.HTTPBearerAuth.__init__', side_effect=TypeError("Invalid token type")):
            HTTPBearerAuth(12345)
