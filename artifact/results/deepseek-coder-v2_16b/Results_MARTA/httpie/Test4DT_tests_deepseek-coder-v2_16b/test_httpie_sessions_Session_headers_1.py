
import pytest
from pathlib import Path
from httpie.sessions import Session

def test_session_creation():
    session = Session(path=Path('test_session.json'))
    assert hasattr(session, 'path'), "Session should have a 'path' attribute"
    assert isinstance(session.path, Path), "'path' should be an instance of Path"


def test_default_headers():
    session = Session(path=Path('test_session.json'))
    assert session['headers'] == {}, "Default headers should be an empty dictionary"

def test_update_headers():
    session = Session(path=Path('test_session.json'))
    updated_headers = {'User-Agent': 'HTTPie/1.0'}
    session['headers'] = updated_headers
    assert session['headers'] == updated_headers, "Headers should be updated correctly"

def test_default_cookies():
    session = Session(path=Path('test_session.json'))
    assert session['cookies'] == {}, "Default cookies should be an empty dictionary"

def test_update_cookies():
    session = Session(path=Path('test_session.json'))
    updated_cookies = {'session_id': 'abc123'}
    session['cookies'] = updated_cookies
    assert session['cookies'] == updated_cookies, "Cookies should be updated correctly"

def test_default_auth():
    session = Session(path=Path('test_session.json'))
    assert session['auth'] == {'type': None, 'username': None, 'password': None}, "Default auth should match the defined structure"

def test_update_auth():
    session = Session(path=Path('test_session.json'))
    updated_auth = {'type': 'basic', 'username': 'user', 'password': 'pass'}
    session['auth'] = updated_auth
    assert session['auth'] == updated_auth, "Authentication should be updated correctly"