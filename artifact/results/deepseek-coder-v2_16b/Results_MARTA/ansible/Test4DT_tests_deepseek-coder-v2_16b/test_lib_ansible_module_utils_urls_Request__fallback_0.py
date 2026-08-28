
import pytest
from ansible.module_utils.urls import Request, cookiejar

def test_valid_inputs():
    r = Request(headers={'Content-Type': 'application/json'}, use_proxy=True, force=False, timeout=10, validate_certs=True,
                 url_username='user', url_password='passwd', http_agent='testAgent', force_basic_auth=False,
                 follow_redirects='urllib2', client_cert=None, client_key=None, cookies=None, unix_socket=None, ca_path=None)
    
    assert r.headers == {'Content-Type': 'application/json'}
    assert r.use_proxy is True
    assert r.force is False
    assert r.timeout == 10
    assert r.validate_certs is True
    assert r.url_username == 'user'
    assert r.url_password == 'passwd'
    assert r.http_agent == 'testAgent'
    assert r.force_basic_auth is False
    assert r.follow_redirects == 'urllib2'
    assert r.client_cert is None
    assert r.client_key is None
    assert isinstance(r.cookies, cookiejar.CookieJar)

def test_edge_cases():
    r = Request()
    
    assert r.headers == {}
    assert r.use_proxy is True
    assert r.force is False
    assert r.timeout == 10
    assert r.validate_certs is True
    assert r.url_username is None
    assert r.url_password is None
    assert r.http_agent is None
    assert r.force_basic_auth is False
    assert r.follow_redirects == 'urllib2'
    assert r.client_cert is None
    assert r.client_key is None
    assert isinstance(r.cookies, cookiejar.CookieJar)
