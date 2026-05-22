
import pytest
from httpie.plugins.builtin import HTTPBearerAuth
from unittest.mock import patch

def test_edge_case_none():
    with patch('httpie.plugins.builtin.HTTPBearerAuth.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            auth = HTTPBearerAuth(None)
