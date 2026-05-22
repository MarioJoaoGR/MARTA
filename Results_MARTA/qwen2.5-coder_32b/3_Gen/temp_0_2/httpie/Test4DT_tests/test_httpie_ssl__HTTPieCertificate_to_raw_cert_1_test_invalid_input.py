
import pytest
from unittest.mock import patch
from httpie.ssl_ import HTTPieCertificate

def test_invalid_input():
    with patch('httpie.ssl_.HTTPieCertificate.to_raw_cert', side_effect=FileNotFoundError):
        cert = HTTPieCertificate()
        with pytest.raises(FileNotFoundError):
            cert.to_raw_cert()
