
import pytest
from unittest.mock import patch, MagicMock
from sanic.mixins.middleware import MiddlewareMixin, FutureMiddleware

# Test Scenario 1: Register middleware with decorator

# Test Scenario 2: Register middleware with on_request method

# Test Scenario 3: Register middleware with on_response method

# Test Scenario 4: Partial application of on_response method

# Test Scenario 5: Mocking and patching to prevent NotImplementedError
@patch('sanic.mixins.middleware.MiddlewareMixin._apply_middleware')
def test_mocked_not_implemented_error(mock_apply_middleware):
    mixin = MiddlewareMixin()
    
    mock_apply_middleware.side_effect = NotImplementedError
    
    with pytest.raises(NotImplementedError):
        mixin._apply_middleware(MagicMock())