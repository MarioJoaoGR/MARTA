
import pytest
from urllib import parse as urlparse
from urllib.parse import urlencode, urlsplit, urlunsplit

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

def test_invalid_input():
    with pytest.raises(TypeError):
        update_query_params(12345, {'foo': 'bar'})  # Invalid URL type

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

../../../dev F                                                           [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
>           update_query_params(12345, {'foo': 'bar'})  # Invalid URL type

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_3_test_invalid_input.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_3_test_invalid_input.py:20: in update_query_params
    scheme, netloc, path, query_string, fragment = urlparse.urlsplit(url)
/usr/local/lib/python3.11/urllib/parse.py:491: in urlsplit
    url, scheme, _coerce_result = _coerce_args(url, scheme)
/usr/local/lib/python3.11/urllib/parse.py:133: in _coerce_args
    return _decode_args(args) + (_encode_result,)
/usr/local/lib/python3.11/urllib/parse.py:117: in _decode_args
    return tuple(x.decode(encoding, errors) if x else '' for x in args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <tuple_iterator object at 0x7fe8009642e0>

>   return tuple(x.decode(encoding, errors) if x else '' for x in args)
E   AttributeError: 'int' object has no attribute 'decode'

/usr/local/lib/python3.11/urllib/parse.py:117: AttributeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-_nzypvzg'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-5229yol0'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-8_bm5k4x'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_input - AttributeError: 'int' object has n...
======================== 1 failed, 3 warnings in 0.10s =========================
"""