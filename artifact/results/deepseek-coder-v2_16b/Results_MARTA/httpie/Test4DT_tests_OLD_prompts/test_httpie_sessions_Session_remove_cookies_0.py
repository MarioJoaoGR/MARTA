
import pytest
from unittest.mock import patch
from httpie.sessions import Session
from pathlib import Path
from typing import Iterable, Union



def test_remove_cookies_valid():
    with patch('httpie.sessions.Session.__init__', return_value=None):
        s = Session(Path('session_data'))
        s['headers'] = {'User-Agent': 'HTTPie/1.0'}
        s['cookies'] = {'session_id': 'abc123'}
        
        assert len(s['cookies']) == 1, "Expected cookies to be present"
        
        s.remove_cookies(['session_id'])
        
        assert not hasattr(s, 'cookies') or len(s['cookies']) == 0, "Expected cookies to be removed"