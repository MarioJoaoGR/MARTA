
import pytest
from httpie.core import decode_raw_args
from typing import List, Union

def test_decode_raw_args_with_all_bytes():
    result = decode_raw_args([b'Hello', b'World'], 'utf-8')
    assert result == ['Hello', 'World']

def test_decode_raw_args_with_all_strings():
    result = decode_raw_args(['Hello', 'World'], 'utf-8')
    assert result == ['Hello', 'World']
