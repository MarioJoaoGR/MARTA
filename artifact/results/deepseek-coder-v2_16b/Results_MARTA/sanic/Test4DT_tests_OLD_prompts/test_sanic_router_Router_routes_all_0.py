
import pytest
from unittest.mock import patch
from sanic.router import Router, MethodNotSupported

# Test case for initializing the Router with invalid parameters
def test_invalid_init():
    with pytest.raises(TypeError):
        router = Router(DEFAULT_METHOD=None, ALLOWED_METHODS=[])
