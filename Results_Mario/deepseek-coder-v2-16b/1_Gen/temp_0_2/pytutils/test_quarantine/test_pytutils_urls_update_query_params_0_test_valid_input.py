
import pytest
from urllib import parse as urlparse
from urllib.parse import urlencode

def update_query_params(url, params, doseq=True):
    """
    Update and/or insert query parameters in a URL.

    >>> update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))
    'http://example.com?...foo=stuff...'

    :param url: URL
    :type url: str
    :param kwargs: Query parameters
    :type kwargs: dict
    :return: Modified URL
    :rtype: str
    """
    scheme, netloc, path, query_string, fragment = urlparse.urlsplit(url)

    query_params = urlparse.parse_qs(query_string)
    query_params.update(**params)

    new_query_string = urlencode(query_params, doseq=doseq)

    new_url = urlparse.urlunsplit([scheme, netloc, path, new_query_string, fragment])
    return new_url

@pytest.mark.parametrize("url, params, expected", [
    ('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}, 'http://example.com/?foo=stuff&biz=baz'),
    ('http://example.com?foo=bar&biz=baz', {'new_param': 'value'}, 'http://example.com/?foo=bar&biz=baz&new_param=value'),
    ('http://example.com?foo=bar&biz=baz', {'foo': ['stuff1', 'stuff2']}, 'http://example.com/?foo=stuff1,stuff2&biz=baz'),
    ('http://example.com?foo=bar', {'foo': 'new_value'}, 'http://example.com/?foo=new_value'),
    ('http://example.com?', {'foo': 'bar'}, 'http://example.com/?foo=bar'),
])
def test_valid_input(url, params, expected):
    assert update_query_params(url, params) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_ test_valid_input[http://example.com?foo=bar&biz=baz-params0-http://example.com/?foo=stuff&biz=baz] _

url = 'http://example.com?foo=bar&biz=baz', params = {'foo': 'stuff'}
expected = 'http://example.com/?foo=stuff&biz=baz'

    @pytest.mark.parametrize("url, params, expected", [
        ('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}, 'http://example.com/?foo=stuff&biz=baz'),
        ('http://example.com?foo=bar&biz=baz', {'new_param': 'value'}, 'http://example.com/?foo=bar&biz=baz&new_param=value'),
        ('http://example.com?foo=bar&biz=baz', {'foo': ['stuff1', 'stuff2']}, 'http://example.com/?foo=stuff1,stuff2&biz=baz'),
        ('http://example.com?foo=bar', {'foo': 'new_value'}, 'http://example.com/?foo=new_value'),
        ('http://example.com?', {'foo': 'bar'}, 'http://example.com/?foo=bar'),
    ])
    def test_valid_input(url, params, expected):
>       assert update_query_params(url, params) == expected
E       AssertionError: assert 'http://examp...stuff&biz=baz' == 'http://examp...stuff&biz=baz'
E         
E         - http://example.com/?foo=stuff&biz=baz
E         ?                   -
E         + http://example.com?foo=stuff&biz=baz

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py:38: AssertionError
_ test_valid_input[http://example.com?foo=bar&biz=baz-params1-http://example.com/?foo=bar&biz=baz&new_param=value] _

url = 'http://example.com?foo=bar&biz=baz', params = {'new_param': 'value'}
expected = 'http://example.com/?foo=bar&biz=baz&new_param=value'

    @pytest.mark.parametrize("url, params, expected", [
        ('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}, 'http://example.com/?foo=stuff&biz=baz'),
        ('http://example.com?foo=bar&biz=baz', {'new_param': 'value'}, 'http://example.com/?foo=bar&biz=baz&new_param=value'),
        ('http://example.com?foo=bar&biz=baz', {'foo': ['stuff1', 'stuff2']}, 'http://example.com/?foo=stuff1,stuff2&biz=baz'),
        ('http://example.com?foo=bar', {'foo': 'new_value'}, 'http://example.com/?foo=new_value'),
        ('http://example.com?', {'foo': 'bar'}, 'http://example.com/?foo=bar'),
    ])
    def test_valid_input(url, params, expected):
>       assert update_query_params(url, params) == expected
E       AssertionError: assert 'http://examp...w_param=value' == 'http://examp...w_param=value'
E         
E         - http://example.com/?foo=bar&biz=baz&new_param=value
E         ?                   -
E         + http://example.com?foo=bar&biz=baz&new_param=value

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py:38: AssertionError
_ test_valid_input[http://example.com?foo=bar&biz=baz-params2-http://example.com/?foo=stuff1,stuff2&biz=baz] _

url = 'http://example.com?foo=bar&biz=baz'
params = {'foo': ['stuff1', 'stuff2']}
expected = 'http://example.com/?foo=stuff1,stuff2&biz=baz'

    @pytest.mark.parametrize("url, params, expected", [
        ('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}, 'http://example.com/?foo=stuff&biz=baz'),
        ('http://example.com?foo=bar&biz=baz', {'new_param': 'value'}, 'http://example.com/?foo=bar&biz=baz&new_param=value'),
        ('http://example.com?foo=bar&biz=baz', {'foo': ['stuff1', 'stuff2']}, 'http://example.com/?foo=stuff1,stuff2&biz=baz'),
        ('http://example.com?foo=bar', {'foo': 'new_value'}, 'http://example.com/?foo=new_value'),
        ('http://example.com?', {'foo': 'bar'}, 'http://example.com/?foo=bar'),
    ])
    def test_valid_input(url, params, expected):
>       assert update_query_params(url, params) == expected
E       AssertionError: assert 'http://examp...tuff2&biz=baz' == 'http://examp...tuff2&biz=baz'
E         
E         - http://example.com/?foo=stuff1,stuff2&biz=baz
E         ?                   -           ^
E         + http://example.com?foo=stuff1&foo=stuff2&biz=baz
E         ?                              ^^^^^

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py:38: AssertionError
_ test_valid_input[http://example.com?foo=bar-params3-http://example.com/?foo=new_value] _

url = 'http://example.com?foo=bar', params = {'foo': 'new_value'}
expected = 'http://example.com/?foo=new_value'

    @pytest.mark.parametrize("url, params, expected", [
        ('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}, 'http://example.com/?foo=stuff&biz=baz'),
        ('http://example.com?foo=bar&biz=baz', {'new_param': 'value'}, 'http://example.com/?foo=bar&biz=baz&new_param=value'),
        ('http://example.com?foo=bar&biz=baz', {'foo': ['stuff1', 'stuff2']}, 'http://example.com/?foo=stuff1,stuff2&biz=baz'),
        ('http://example.com?foo=bar', {'foo': 'new_value'}, 'http://example.com/?foo=new_value'),
        ('http://example.com?', {'foo': 'bar'}, 'http://example.com/?foo=bar'),
    ])
    def test_valid_input(url, params, expected):
>       assert update_query_params(url, params) == expected
E       AssertionError: assert 'http://examp...foo=new_value' == 'http://examp...foo=new_value'
E         
E         - http://example.com/?foo=new_value
E         ?                   -
E         + http://example.com?foo=new_value

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py:38: AssertionError
__ test_valid_input[http://example.com?-params4-http://example.com/?foo=bar] ___

url = 'http://example.com?', params = {'foo': 'bar'}
expected = 'http://example.com/?foo=bar'

    @pytest.mark.parametrize("url, params, expected", [
        ('http://example.com?foo=bar&biz=baz', {'foo': 'stuff'}, 'http://example.com/?foo=stuff&biz=baz'),
        ('http://example.com?foo=bar&biz=baz', {'new_param': 'value'}, 'http://example.com/?foo=bar&biz=baz&new_param=value'),
        ('http://example.com?foo=bar&biz=baz', {'foo': ['stuff1', 'stuff2']}, 'http://example.com/?foo=stuff1,stuff2&biz=baz'),
        ('http://example.com?foo=bar', {'foo': 'new_value'}, 'http://example.com/?foo=new_value'),
        ('http://example.com?', {'foo': 'bar'}, 'http://example.com/?foo=bar'),
    ])
    def test_valid_input(url, params, expected):
>       assert update_query_params(url, params) == expected
E       AssertionError: assert 'http://example.com?foo=bar' == 'http://example.com/?foo=bar'
E         
E         - http://example.com/?foo=bar
E         ?                   -
E         + http://example.com?foo=bar

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py:38: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py::test_valid_input[http:/example.com?foo=bar&biz=baz-params0-http:/example.com/?foo=stuff&biz=baz]
FAILED pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py::test_valid_input[http:/example.com?foo=bar&biz=baz-params1-http:/example.com/?foo=bar&biz=baz&new_param=value]
FAILED pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py::test_valid_input[http:/example.com?foo=bar&biz=baz-params2-http:/example.com/?foo=stuff1,stuff2&biz=baz]
FAILED pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py::test_valid_input[http:/example.com?foo=bar-params3-http:/example.com/?foo=new_value]
FAILED pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_0_test_valid_input.py::test_valid_input[http:/example.com?-params4-http:/example.com/?foo=bar]
============================== 5 failed in 0.06s ===============================
"""