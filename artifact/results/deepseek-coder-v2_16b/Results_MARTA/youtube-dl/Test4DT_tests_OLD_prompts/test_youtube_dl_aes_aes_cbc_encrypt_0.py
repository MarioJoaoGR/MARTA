
import pytest
from unittest.mock import patch
from math import ceil
from youtube_dl.aes import aes_encrypt

BLOCK_SIZE_BYTES = 16

def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]

def key_expansion(key):
    # Placeholder for actual key expansion logic
    return key

def aes_cbc_encrypt(data, key, iv):
    expanded_key = key_expansion(key)
    block_count = int(ceil(float(len(data)) / BLOCK_SIZE_BYTES))

    encrypted_data = []
    previous_cipher_block = iv
    for i in range(block_count):
        block = data[i * BLOCK_SIZE_BYTES: (i + 1) * BLOCK_SIZE_BYTES]
        remaining_length = BLOCK_SIZE_BYTES - len(block)
        block += [remaining_length] * remaining_length
        mixed_block = xor(block, previous_cipher_block)

        encrypted_block = aes_encrypt(mixed_block, expanded_key)
        encrypted_data += encrypted_block

        previous_cipher_block = encrypted_block

    return encrypted_data

def test_valid_input():
    data = [0] * 16
    key = [0] * 16
    iv = [0] * 16
    
    with patch('youtube_dl.aes.aes_encrypt', side_effect=[i for i in range(16)]):
        encrypted_data = aes_cbc_encrypt(data, key, iv)
        assert len(encrypted_data) == BLOCK_SIZE_BYTES
