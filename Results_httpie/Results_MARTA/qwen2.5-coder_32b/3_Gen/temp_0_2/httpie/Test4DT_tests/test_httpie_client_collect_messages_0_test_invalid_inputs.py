
import pytest
from unittest.mock import patch, MagicMock
from httpie.client import collect_messages
from httpie.sessions import Environment
import argparse

def test_invalid_inputs():
    # Create a mock environment and arguments
    env = Environment()
    args = argparse.Namespace(session=None, session_read_only=None)

    with patch('httpie.client.get_httpie_session') as mock_get_httpie_session:
        # Mock the get_httpie_session to return a mock session
        mock_session = MagicMock()
        mock_get_httpie_session.return_value = mock_session

        # Call the function with invalid inputs (None for both session and session_read_only)
        with pytest.raises(AttributeError):
            list(collect_messages(env, args))
