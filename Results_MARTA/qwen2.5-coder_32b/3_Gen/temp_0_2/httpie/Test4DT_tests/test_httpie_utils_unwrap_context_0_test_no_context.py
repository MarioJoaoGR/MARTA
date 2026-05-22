
import unittest
from unittest.mock import patch
from httpie.utils import unwrap_context

class TestHttpieUtilsUnwrapContext(unittest.TestCase):
    def test_no_context(self):
        try:
            raise ValueError("Root error") from FileNotFoundError("Related error")
        except ValueError as e:
            with patch('httpie.utils.unwrap_context', return_value=e) as mock_unwrap:
                unwrapped_exc = unwrap_context(e)
                self.assertIsInstance(unwrapped_exc, ValueError)
