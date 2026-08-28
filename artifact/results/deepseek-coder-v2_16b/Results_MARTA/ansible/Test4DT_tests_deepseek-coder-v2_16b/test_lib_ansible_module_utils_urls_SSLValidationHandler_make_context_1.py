
import pytest
from ssl_validation_handler import SSLValidationHandler

# Fixture to create instances for testing
@pytest.fixture(params=[
    ('example.com', 443, '/path/to/ca/bundle'),
    ('another-example.com', 4433, None),
    (None, -1, None)
])
def ssl_handler_instance(request):
    hostname, port, ca_path = request.param
    return SSLValidationHandler(hostname, port, ca_path)

# Test scenarios
def test_valid_inputs(ssl_handler_instance):
    assert isinstance(ssl_handler_instance, SSLValidationHandler)
    assert ssl_handler_instance.hostname == 'example.com' or None
    assert ssl_handler_instance.port == 443 or -1
    assert ssl_handler_instance.ca_path == '/path/to/ca/bundle' or None

def test_edge_cases(ssl_handler_instance):
    if ssl_handler_instance.ca_path is None:
        with pytest.raises(ValueError):
            SSLValidationHandler('example.com', 443, None)
    else:
        assert isinstance(ssl_handler_instance, SSLValidationHandler)

def test_invalid_inputs():
    with pytest.raises(ValueError):
        SSLValidationHandler(None, -1)
