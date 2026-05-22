
import pytest
from httpie.ssl_ import HTTPieCertificate

def test_invalid_inputs():
    cert = HTTPieCertificate()
    
    with pytest.raises(AttributeError):
        # Test when cert_file is not a string
        cert.cert_file = 12345
