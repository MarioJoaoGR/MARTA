
import unittest
from unittest.mock import patch
from pathlib import Path
from httpie.sessions import Environment, Session

class TestSessionInit(unittest.TestCase):
    @patch('httpie.sessions.Environment')
    def test_invalid_inputs(self, mock_env):
        # Arrange
        invalid_path = 12345  # Invalid path type
        invalid_session_id = None  # Invalid session ID type
        
        # Act and Assert
        with self.assertRaises(TypeError):
            Session(path=invalid_path, env=mock_env, bound_host='example.com', session_id=invalid_session_id)
