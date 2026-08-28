
import pytest
from unittest.mock import patch, MagicMock
from httpie.sessions import Session
from pathlib import Path


def test_none_input():
    with patch('httpie.sessions.Session', autospec=True) as mock_session:
        with pytest.raises(TypeError):
            session = Session(path=None)