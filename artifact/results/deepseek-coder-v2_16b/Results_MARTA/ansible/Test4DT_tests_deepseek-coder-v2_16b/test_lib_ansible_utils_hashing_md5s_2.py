
import pytest
from hashlib import md5

def test_valid_input_string():
    data = 'hello world'
    expected_hash = md5(data.encode()).hexdigest()
    assert md5s(data) == expected_hash

def test_valid_input_bytes():
    data = b'hello world'
    expected_hash = md5(data).hexdigest()
    assert md5s(data) == expected_hash

def test_invalid_input():
    data = 12345
    with pytest.raises(ValueError):
        md5s(data)
