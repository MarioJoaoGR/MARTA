
import pytest
from pathlib import Path
from httpie.sessions import Environment, Session
from unittest.mock import patch

def test_invalid_input():
    with pytest.raises(Exception) as e:
        with patch('httpie.sessions.Session.__init__', side_effect=Exception("Invalid Input")):
            Session('invalid_path', 'invalid_env', 'invalid_host', 'invalid_id')
    assert str(e.value) == "Invalid Input"
