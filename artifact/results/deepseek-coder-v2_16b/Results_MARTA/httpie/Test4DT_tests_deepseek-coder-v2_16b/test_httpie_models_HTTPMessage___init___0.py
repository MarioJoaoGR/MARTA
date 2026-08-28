
import pytest
from httpie.models import HTTPMessage

def test_none_input():
    with pytest.raises(TypeError):
        HTTPMessage()
