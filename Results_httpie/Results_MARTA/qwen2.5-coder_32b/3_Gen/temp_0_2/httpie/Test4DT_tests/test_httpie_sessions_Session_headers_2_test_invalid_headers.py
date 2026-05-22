
import pytest
from pathlib import Path
from httpie.sessions import Environment, Session
from unittest.mock import patch

def test_invalid_headers():
    with patch('httpie.sessions.Session.__init__', side_effect=ImportError):
        with pytest.raises(ImportError):
            session = Session(path=Path('session_file'), env=Environment(), bound_host='example.com', session_id='12345')
