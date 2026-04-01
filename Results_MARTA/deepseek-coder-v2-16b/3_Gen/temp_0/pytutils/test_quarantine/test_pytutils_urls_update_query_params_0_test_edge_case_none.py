
import pytest
from pytutils.urls import update_query_params

def test_update_query_params():
    # Test adding a new parameter to an existing URL with query parameters
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'newparam': 'value'}
    expected_url = 'http://example.com?foo=bar&biz=baz&newparam=value'
    assert update_query_params(url, params) == expected_url

    # Test updating an existing parameter in the URL
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    expected_url = 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params(url, params) == expected_url

    # Test adding a new parameter without replacing existing ones
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'newparam': ['value1', 'value2']}
    expected_url = 'http://example.com?foo=bar&biz=baz&newparam=value1&newparam=value2'
    assert update_query_params(url, params) == expected_url

    # Test adding a new parameter with doseq=False
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'newparam': ['value1', 'value2']}
    expected_url = 'http://example.com?foo=bar&biz=baz&newparam=value1,value2'
    assert update_query_params(url, params, doseq=False) == expected_url

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""