
import pytest
from requests_toolbelt import MultipartEncoder
from unittest.mock import patch, MagicMock

def get_multipart_data_and_content_type(data):
    if not data:
        raise ValueError('Invalid input data')
    encoder = MultipartEncoder(fields=data.items())
    return encoder, f'multipart/form-data; boundary={encoder.boundary}'

def test_invalid_input():
    with pytest.raises(ValueError) as e:
        get_multipart_data_and_content_type({})
    assert str(e.value) == 'Invalid input data'
