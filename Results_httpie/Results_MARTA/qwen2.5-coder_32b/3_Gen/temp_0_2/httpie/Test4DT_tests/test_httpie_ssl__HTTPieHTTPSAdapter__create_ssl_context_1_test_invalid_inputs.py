
import pytest
from unittest.mock import patch
from httpie.ssl_ import HTTPieHTTPSAdapter
from requests import Session

def test_invalid_inputs():
    session = Session()
    with pytest.raises(Exception):
        session.mount('https://', HTTPieHTTPSAdapter(verify=False, ssl_version='invalid', ciphers='invalid'))
