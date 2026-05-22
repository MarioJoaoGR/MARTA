
import pytest
from pathlib import Path
from httpie.sessions import Environment, Session
from unittest.mock import patch

def test_invalid_input():
    with pytest.raises(TypeError):
        with patch('httpie.sessions.Session.__init__', side_effect=TypeError("Invalid input")):
            Session(path=123, env='env', bound_host=True, session_id=[1, 2, 3])
