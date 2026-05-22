
import pytest
from unittest.mock import patch
from httpie.utils import unwrap_context

def test_valid_input():
    try:
        raise ValueError("Root error") from FileNotFoundError("Related error")
    except ValueError as e:
        unwrapped_exc = unwrap_context(e)
        assert isinstance(unwrapped_exc, ValueError), "Expected the original exception to be a ValueError"
