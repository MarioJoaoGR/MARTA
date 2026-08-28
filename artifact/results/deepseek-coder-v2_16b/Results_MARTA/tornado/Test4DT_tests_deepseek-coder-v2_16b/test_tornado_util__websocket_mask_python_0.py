
import pytest
from tornado.util import _websocket_mask_python



def test_valid_data_and_mask():
    mask = b'abcd'
    data = b'hello'
    expected_output = bytes([b ^ mask[i % 4] for i, b in enumerate(data)])
    assert _websocket_mask_python(mask, data) == expected_output