
import pytest
from unittest.mock import patch
from math import ceil
from youtube_dl.aes import key_expansion, aes_decrypt, xor

# Define BLOCK_SIZE_BYTES as 16 for AES block size in bytes
BLOCK_SIZE_BYTES = 16

def aes_cbc_decrypt(data, key, iv):
    """
    Decrypts data that was encrypted using AES in CBC mode. This function takes a byte array representing ciphertext, a key used for encryption (which should be 16, 24, or 32 bytes long), and an initialization vector (IV) of the same length as a block size (16 bytes).
    
    Parameters:
        data (list of int): A list of integers representing the ciphertext to be decrypted. Each integer should represent a byte in the range [0, 255].
        
        key (list of int): A list of integers representing the encryption key. The length of this list should be either 16, 24, or 32 bytes (corresponding to AES-128, AES-192, and AES-256 respectively).
        
        iv (list of int): A list of integers representing the initialization vector used in CBC mode. The length of this list should be exactly 16 bytes.
        
    Returns:
        list of int: A list of integers representing the decrypted plaintext data, with each byte in the range [0, 255].
    
    Examples:
        >>> aes_cbc_decrypt([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0] * 16, [0] * 16)
        [decrypted data]
        
    Notes:
        - The function first expands the key using `key_expansion`.
        - It then decrypts each block of ciphertext in CBC mode by XORing the decrypted block with the previous cipher block and appending it to the result.
        - If the length of the data is not a multiple of 16, the last block is padded with zeros to ensure all blocks are processed correctly.
        - Ensure that the `key_expansion`, `aes_decrypt`, `xor` functions are defined elsewhere in your codebase and operate as expected for their respective tasks.
    """
    expanded_key = key_expansion(key)
    block_count = int(ceil(float(len(data)) / BLOCK_SIZE_BYTES))

    decrypted_data = []
    previous_cipher_block = iv
    for i in range(block_count):
        block = data[i * BLOCK_SIZE_BYTES: (i + 1) * BLOCK_SIZE_BYTES]
        block += [0] * (BLOCK_SIZE_BYTES - len(block))

        decrypted_block = aes_decrypt(block, expanded_key)
        decrypted_data += xor(decrypted_block, previous_cipher_block)
        previous_cipher_block = block
    decrypted_data = decrypted_data[:len(data)]

    return decrypted_data

# Test cases for aes_cbc_decrypt function
def test_aes_cbc_decrypt_with_valid_data():
    data = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    key = [0] * 16
    iv = [0] * 16
    
    with patch('youtube_dl.aes.key_expansion', return_value=[0]*16*8):  # Mock key expansion
        with patch('youtube_dl.aes.aes_decrypt', side_effect=lambda x, y: [x[i] ^ y for i in range(len(x))]):  # Mock AES decrypt
            with patch('youtube_dl.aes.xor', return_value=[0]*16):  # Mock XOR function
                decrypted = aes_cbc_decrypt(data, key, iv)
                assert len(decrypted) == len(data), "Decrypted data length does not match the original data length"
