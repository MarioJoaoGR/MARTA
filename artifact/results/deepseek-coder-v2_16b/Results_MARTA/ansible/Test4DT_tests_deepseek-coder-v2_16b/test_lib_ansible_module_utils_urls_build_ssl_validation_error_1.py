
import pytest
from ansible.module_utils.urls import urllib_request
try:
    from ansible.modules.network.validation import build_ssl_validation_error, SSLValidationError
except ImportError:
    # If the module is not available in the environment, we can't run these tests
    pytestmark = pytest.mark.skip(reason="SSLValidationError and related imports are unavailable")

def test_valid_input():
    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error('example.com', 443, ['https://example.com'])
    assert "Failed to validate the SSL certificate for example.com:443." in str(excinfo.value)
    assert "Make sure your managed systems have a valid CA" in str(excinfo.value)
    assert "Paths checked for this platform: https://example.com." in str(excinfo.value)

def test_edge_case_none():
    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(None, None, [])
    assert "Failed to validate the SSL certificate for None:None." in str(excinfo.value)
    assert "Make sure your managed systems have a valid CA" in str(excinfo.value)
    assert "Paths checked for this platform: ." in str(excinfo.value)

def test_invalid_input():
    try:
        build_ssl_validation_error('example.com', 443, ['https://example.com'], exc=ValueError('Invalid certificate'))
    except SSLValidationError as e:
        assert "Failed to validate the SSL certificate for example.com:443." in str(e)
        assert "Make sure your managed systems have a valid CA" in str(e)
        assert "Paths checked for this platform: https://example.com." in str(e)
        assert "The exception msg was: Invalid certificate." in str(e)
