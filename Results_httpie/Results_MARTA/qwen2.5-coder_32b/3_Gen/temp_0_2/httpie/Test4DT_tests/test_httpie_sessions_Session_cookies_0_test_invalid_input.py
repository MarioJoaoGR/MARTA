
import pytest
from pathlib import Path
from httpie.sessions import Environment, Session
from unittest.mock import patch

def test_invalid_input():
    with pytest.raises(TypeError):
        with patch('httpie.sessions.Session.__init__', side_effect=TypeError("Invalid input type")):
            session = Session(
                path="invalid_path",
                env=Environment(),
                bound_host='example.com',
                session_id='12345'
            )
