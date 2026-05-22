
import pytest
from unittest.mock import patch
from httpie.ssl_ import HTTPieCertificate

def test_none_input():
    with patch('httpie.ssl_.HTTPieCertificate') as mock_cert:
        # Create an instance of HTTPieCertificate
        cert = HTTPieCertificate()
        
        # Call the to_raw_cert method
        raw_cert = cert.to_raw_cert()
        
        # Assert that the output is a tuple with None values
        assert raw_cert == (None, None)
