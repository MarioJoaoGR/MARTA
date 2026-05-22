
import unittest.mock as mock
from httpie.utils import unwrap_context

def test_no_context():
    try:
        raise ValueError("Root error") from FileNotFoundError("Related error")
    except ValueError as e:
        with mock.patch('httpie.utils.unwrap_context', return_value=e):
            unwrapped_exc = unwrap_context(e)
            assert isinstance(unwrapped_exc, ValueError), "Expected the original ValueError"
