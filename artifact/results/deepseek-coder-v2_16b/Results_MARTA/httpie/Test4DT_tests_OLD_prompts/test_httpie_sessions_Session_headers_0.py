
import pytest
from httpie.sessions import Session
from pathlib import Path
from unittest.mock import patch, MagicMock



def test_invalid_input():
    with patch('httpie.sessions.Session', autospec=True) as mock_session:
        with pytest.raises(Exception):
            session = Session()