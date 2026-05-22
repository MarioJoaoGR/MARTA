
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPResponse

def test_invalid_input():
    with patch('httpie.models.HTTPResponse.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            response = MagicMock()
            HTTPResponse(response)
