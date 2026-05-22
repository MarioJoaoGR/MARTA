
import unittest
from unittest.mock import patch, MagicMock
from httpie.internal.update_warnings import Environment

class TestHttpieInternalUpdateWarnings(unittest.TestCase):
    @patch('httpie.internal.update_warnings.Environment')
    def test_invalid_input_error_handling(self, MockEnvClass):
        # Create a mock environment object with developer mode enabled
        env = MockEnvClass.return_value
        env.config.developer_mode = True
        
        from httpie.internal.update_warnings import _get_suppress_context
        ctx_mgr = _get_suppress_context(env)
        
        with self.assertRaises(ValueError):
            with ctx_mgr:
                raise ValueError("Test Error")
