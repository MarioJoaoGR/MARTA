
import pytest
from cryptography import x509, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import UnsupportedAlgorithm

# Fixture to provide a valid DER-encoded X.509 certificate
@pytest.fixture(scope="module")
def valid_certificate():
    # Example of a valid DER-encoded X.509 certificate
    return b'...'  # Replace with actual valid certificate data

# Test for a valid DER-encoded X.509 certificate
def test_valid_certificate(valid_certificate):
    hashed_value = get_channel_binding_cert_hash(valid_certificate)
    assert isinstance(hashed_value, bytes), "Expected bytes output"
    assert len(hashed_value) == hashes.SHA256().digest_size, "Unexpected hash length"

# Test for None input
def test_none_input():
    with pytest.raises(TypeError):
        get_channel_binding_cert_hash(None)

# Test for an empty DER-encoded X.509 certificate
@pytest.fixture(scope="module")
def empty_certificate():
    return b''

def test_empty_certificate(empty_certificate):
    with pytest.raises(x509.LoadingError):
        get_channel_binding_cert_hash(empty_certificate)
