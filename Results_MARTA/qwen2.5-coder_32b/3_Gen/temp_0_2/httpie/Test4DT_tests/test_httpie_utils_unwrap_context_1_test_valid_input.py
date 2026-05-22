
import pytest
from unittest.mock import patch
from httpie.utils import unwrap_context

def test_valid_input():
    exc = ValueError('Root error')
    exc.__context__ = FileNotFoundError('Related error')
    
    with patch('httpie.utils.unwrap_context', return_value=exc):
        result = unwrap_context(exc)
        assert isinstance(result, ValueError)
