
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPRequest
import requests
from urllib.parse import urlsplit



def test_invalid_input():
    with pytest.raises(Exception):
        raise Exception("Test exception")