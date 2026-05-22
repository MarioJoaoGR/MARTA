
import pytest
from httpie.uploads import get_multipart_data_and_content_type
from requests_toolbelt import MultipartEncoder
from unittest.mock import patch

@pytest.fixture
def valid_input():
    data = {
        'file': ('example.txt', open('example.txt', 'rb')),
        'description': 'This is a test upload.'
    }
    return get_multipart_data_and_content_type(data)

def test_valid_input(valid_input):
    multipart_data, content_type = valid_input
    assert isinstance(multipart_data, MultipartEncoder)
    assert 'boundary=' in content_type
