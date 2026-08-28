
import pytest
from unittest.mock import patch
from youtube_dl.aes import aes_encrypt, BLOCK_SIZE_BYTES

@pytest.fixture(params=[16, 24, 32])
def expanded_key(request):
    return [0] * request.param

@pytest.mark.parametrize("data", [[0]*BLOCK_SIZE_BYTES for _ in range(3)])
def test_basic_encryption(data, expanded_key):
    encrypted_data = aes_encrypt(data, expanded_key)
    assert len(encrypted_data) == BLOCK_SIZE_BYTES
    assert all(isinstance(x, int) for x in encrypted_data)

@pytest.mark.parametrize("data", [[42]*BLOCK_SIZE_BYTES for _ in range(3)])
def test_realistic_encryption(data, expanded_key):
    encrypted_data = aes_encrypt(data, expanded_key)
    assert len(encrypted_data) == BLOCK_SIZE_BYTES
    assert all(isinstance(x, int) for x in encrypted_data)

@pytest.mark.parametrize("data", [[42]*BLOCK_SIZE_BYTES for _ in range(3)])
def test_aes_version_handling(data, expanded_key):
    if len(expanded_key) == 176:  # AES-128
        assert len(expanded_key) == 176
        encrypted_data = aes_encrypt(data, expanded_key)
        assert len(encrypted_data) == BLOCK_SIZE_BYTES
        assert all(isinstance(x, int) for x in encrypted_data)
    elif len(expanded_key) == 208:  # AES-192
        assert len(expanded_key) == 208
        encrypted_data = aes_encrypt(data, expanded_key)
        assert len(encrypted_data) == BLOCK_SIZE_BYTES
        assert all(isinstance(x, int) for x in encrypted_data)
    elif len(expanded_key) == 240:  # AES-256
        assert len(expanded_key) == 240
        encrypted_data = aes_encrypt(data, expanded_key)
        assert len(encrypted_data) == BLOCK_SIZE_BYTES
        assert all(isinstance(x, int) for x in encrypted_data)
