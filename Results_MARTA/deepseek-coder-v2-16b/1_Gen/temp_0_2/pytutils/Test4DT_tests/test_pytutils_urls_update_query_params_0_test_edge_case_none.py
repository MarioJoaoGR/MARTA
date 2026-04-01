
import pytest
from pytutils.urls import update_query_params
from urllib.parse import urlparse, parse_qs, urlencode, urlsplit

def test_edge_case_none():
    with pytest.raises(TypeError):
        assert update_query_params(None, {'foo': 'bar'}) is None
