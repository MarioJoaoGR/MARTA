
import pytest
from unittest.mock import patch
from youtube_dl.aes import sub_bytes, SBOX


def test_invalid_input():
    with pytest.raises(IndexError):
        data = [256]
        sub_bytes(data)