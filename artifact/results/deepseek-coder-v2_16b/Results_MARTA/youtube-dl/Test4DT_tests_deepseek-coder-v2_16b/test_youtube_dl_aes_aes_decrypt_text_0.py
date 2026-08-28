
import pytest
import base64
from youtube_dl.aes import aes_decrypt_text


def test_invalid_key_size():
    data = 'encryptedData'
    password = 'password'
    key_size_bytes = 24
    with pytest.raises(ValueError):
        aes_decrypt_text(data, password, key_size_bytes)

def test_empty_data():
    data = ''
    password = 'password'
    key_size_bytes = 16
    expected_output = b''
    
    # Encode the data to base64 for comparison
    encoded_data = base64.b64encode(expected_output).decode('utf-8')
    
    assert aes_decrypt_text(encoded_data, password, key_size_bytes) == expected_output