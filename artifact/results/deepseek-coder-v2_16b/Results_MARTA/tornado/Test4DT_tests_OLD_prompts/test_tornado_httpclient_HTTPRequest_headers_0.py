
import pytest
from unittest.mock import patch
from tornado.httpclient import HTTPRequest, HTTPError



def test_invalid_input_missing_url():
    with pytest.raises(TypeError):
        HTTPRequest()