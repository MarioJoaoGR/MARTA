
import pytest
from httpie.core import decode_raw_args
from typing import List, Union

def test_valid_input_all_strings():
    args = ['Hello', 'World']
    result = decode_raw_args(args, 'utf-8')
    assert result == ['Hello', 'World'], f"Expected ['Hello', 'World'], but got {result}"

def test_valid_input_all_bytes():
    args = [b'Hello', b'World']
    result = decode_raw_args(args, 'utf-8')
    assert result == ['Hello', 'World'], f"Expected ['Hello', 'World'], but got {result}"
