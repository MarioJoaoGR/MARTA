
import pytest
from pathlib import Path
from httpie.sessions import Session
from unittest.mock import patch, MagicMock




def test_custom_configuration():
    # Test updating headers and cookies in a Session object
    session = Session('valid_file.json')
    session['headers'] = {'User-Agent': 'HTTPie/1.0'}
    assert session['headers'] == {'User-Agent': 'HTTPie/1.0'}, "Headers should be updated correctly"
    session['cookies'] = {'session_id': 'abc123'}
    assert session['cookies'] == {'session_id': 'abc123'}, "Cookies should be updated correctly"
