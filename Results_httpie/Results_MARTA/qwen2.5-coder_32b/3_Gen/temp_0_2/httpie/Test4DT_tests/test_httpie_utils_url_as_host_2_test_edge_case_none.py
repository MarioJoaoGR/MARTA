
import pytest
from urllib.parse import urlsplit
from unittest.mock import patch

def url_as_host(url: str) -> str:
    return urlsplit(url).netloc.split('@')[-1]

def test_edge_case_none():
    with pytest.raises(TypeError):
        assert url_as_host(None) is None
