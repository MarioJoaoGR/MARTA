
import pytest
from pytutils.urls import update_query_params
from urllib.parse import urlparse, parse_qs, urlencode, urlsplit, urlunsplit

def test_update_query_params():
    # Test with a base URL and parameters to be updated or added
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    expected_url = 'http://example.com?...foo=stuff...'
    
    result = update_query_params(url, params)
    assert result == expected_url

    # Test with a base URL and new parameter to be added
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'newparam': 'value'}
    expected_url = 'http://example.com?...newparam=value...'
    
    result = update_query_params(url, params)
    assert result == expected_url

    # Test with a base URL and parameters to be updated or added, using doseq=False
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'newparam': ['value1', 'value2']}
    expected_url = 'http://example.com?...newparam=value1&newparam=value2...'
    
    result = update_query_params(url, params, doseq=False)
    assert result == expected_url

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""