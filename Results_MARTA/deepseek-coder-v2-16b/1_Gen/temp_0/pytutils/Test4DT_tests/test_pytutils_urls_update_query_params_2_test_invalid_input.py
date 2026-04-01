
import pytest
from urllib import parse as urlparse
from urllib.parse import urlencode

def update_query_params(url, params, doseq=True):
    scheme, netloc, path, query_string, fragment = urlparse.urlsplit(url)
    query_params = urlparse.parse_qs(query_string)
    query_params.update(**params)
    new_query_string = urlencode(query_params, doseq=doseq)
    new_url = urlparse.urlunsplit([scheme, netloc, path, new_query_string, fragment])
    return new_url

def test_invalid_input():
    with pytest.raises(TypeError):
        update_query_params('http://example.com?foo=bar&biz=baz', 123)          # Invalid params type (int)
        update_query_params('http://example.com?foo=bar&biz=baz', {'key': [1, 2]})  # Invalid key type (int in list)
        update_query_params(None, {'foo': 'bar'})                                # Invalid url type (None)
