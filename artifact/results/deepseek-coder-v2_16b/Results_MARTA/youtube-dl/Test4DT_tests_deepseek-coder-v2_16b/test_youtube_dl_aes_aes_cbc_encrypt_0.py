
import pytest
from youtube_dl.aes import aes_cbc_encrypt



def test_valid_encryption():
    data = [i for i in range(16)]
    key = [i for i in range(16)]
    iv = [0] * 16
    
    encrypted_data = aes_cbc_encrypt(data, key, iv)
    assert len(encrypted_data) == len(data)  # Ensure the length of encrypted data matches the input data