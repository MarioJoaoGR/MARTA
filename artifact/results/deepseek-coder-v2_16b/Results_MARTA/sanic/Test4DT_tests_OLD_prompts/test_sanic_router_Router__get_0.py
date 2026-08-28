
import pytest
from unittest.mock import patch
from sanic.router import Router
from sanic.exceptions import MethodNotSupported, NotFound


def test_invalid_path():
    router = Router()
    with patch('sanic.router.Router._get', side_effect=NotFound("Requested URL /nonexistent not found")):
        with pytest.raises(NotFound) as excinfo:
            router._get("/nonexistent", "GET")
    assert str(excinfo.value) == 'Requested URL /nonexistent not found'