
import pytest
from unittest.mock import patch
from youtube_dl.aes import key_expansion, BLOCK_SIZE_BYTES, SBOX, RCON

def test_key_expansion_128bit():
    with patch('youtube_dl.aes.SBOX', [0]*256):  # Mocking SBOX for simplicity
        with patch('youtube_dl.aes.RCON', [0]*11):  # Mocking RCON for simplicity
            key = [0] * 16
            expanded_key = key_expansion(key)
            assert len(expanded_key) == 176

def test_key_expansion_192bit():
    with patch('youtube_dl.aes.SBOX', [0]*256):  # Mocking SBOX for simplicity
        with patch('youtube_dl.aes.RCON', [0]*11):  # Mocking RCON for simplicity
            key = [0] * 24
            expanded_key = key_expansion(key)
            assert len(expanded_key) == 208

def test_key_expansion_256bit():
    with patch('youtube_dl.aes.SBOX', [0]*256):  # Mocking SBOX for simplicity
        with patch('youtube_dl.aes.RCON', [0]*11):  # Mocking RCON for simplicity
            key = [0] * 32
            expanded_key = key_expansion(key)
            assert len(expanded_key) == 240
