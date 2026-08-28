# Module: ansible.module_utils.urls
import pytest
from ansible.module_utils.urls import Request
from http.cookiejar import CookieJar
import requests

# Test default initialization
def test_default_initialization():
    r = Request()
    response = r.open('GET', 'http://httpbin.org/get')
    assert response is not None, "Expected a response but got none"
    assert response.read(), "Expected content in the response but got nothing"

# Test custom headers
def test_custom_headers():
    r = Request(headers={'foo': 'bar'})
    response = r.open('GET', 'http://httpbin.org/get', headers={'baz': 'qux'})
    assert response is not None, "Expected a response but got none"
    assert response.read(), "Expected content in the response but got nothing"
    assert 'foo' in response.headers, "Expected header 'foo' to be present"
    assert response.headers['foo'] == 'bar', "Expected header 'foo' to have value 'bar'"
    assert 'baz' in response.headers, "Expected header 'baz' to be present"
    assert response.headers['baz'] == 'qux', "Expected header 'baz' to have value 'qux'"

# Test basic authentication
def test_basic_authentication():
    r = Request(url_username='user', url_password='passwd')
    response = r.open('GET', 'http://httpbin.org/basic-auth/user/passwd')
    assert response is not None, "Expected a response but got none"
    assert response.read(), "Expected content in the response but got nothing"

# Test custom HTTP method
def test_custom_http_method():
    r = Request()
    response = r.open('POST', 'http://httpbin.org/post', data={'key': 'value'})
    assert response is not None, "Expected a response but got none"
    assert response.read(), "Expected content in the response but got nothing"

# Test using a proxy
def test_using_proxy():
    r = Request(use_proxy=True)
    response = r.open('GET', 'http://httpbin.org/get')
    assert response is not None, "Expected a response but got none"
    assert response.read(), "Expected content in the response but got nothing"

# Test specifying a timeout
def test_specifying_timeout():
    r = Request(timeout=5)
    with pytest.raises(requests.Timeout):
        r.open('GET', 'http://httpbin.org/delay/10')  # This should raise a Timeout

# Test disabling SSL certificate validation
def test_disabling_ssl_certificate_validation():
    r = Request(validate_certs=False)
    with pytest.raises(requests.exceptions.SSLError):
        r.open('GET', 'https://httpbin.org/get')  # This should raise an SSLError

# Test using a Unix domain socket
def test_using_unix_domain_socket():
    r = Request(unix_socket='/path/to/socket')
    with pytest.raises(NotImplementedError):
        r.open('GET', 'http://example.com')  # This should raise NotImplementedError

# Test using a client certificate and key
def test_using_client_certificate_and_key():
    r = Request(client_cert='/path/to/cert', client_key='/path/to/key')
    response = r.open('GET', 'https://httpbin.org/get')
    assert response is not None, "Expected a response but got none"
    assert response.read(), "Expected content in the response but got nothing"

# Test handling cookies
def test_handling_cookies():
    r = Request(cookies=CookieJar())
    response = r.open('GET', 'http://httpbin.org/cookies/set?k1=v1')
    assert response is not None, "Expected a response but got none"
    assert response.read(), "Expected content in the response but got nothing"
    cookies = r.cookies
    assert len(cookies) == 1, "Expected one cookie to be set"
    assert 'k1' in cookies, "Expected cookie 'k1' to be present"
    assert cookies['k1'].value == 'v1', "Expected cookie 'k1' to have value 'v1'"
