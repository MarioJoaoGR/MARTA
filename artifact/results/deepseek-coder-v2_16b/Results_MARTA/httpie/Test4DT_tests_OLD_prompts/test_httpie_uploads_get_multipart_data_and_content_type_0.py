
import pytest
from unittest.mock import patch, MagicMock
from httpie.uploads import get_multipart_data_and_content_type
from requests_toolbelt.multipart.encoder import MultipartEncoder
from typing import Tuple, Dict, Any

# Define a type alias for clarity
MultipartRequestDataDict = Dict[str, Any]

@pytest.fixture(scope="module")
def setup_data():
    return {
        'file1': '/path/to/file1',
        'file2': b'bytes_content_of_file2'
    }



def test_get_multipart_data_and_content_type_with_custom_content_type(setup_data):
    mvod = {key: value for key, value in setup_data.items()}
    encoder, content_type = get_multipart_data_and_content_type(mvod, content_type='multipart/form-data')
    assert isinstance(encoder, MultipartEncoder), "Expected a MultipartEncoder instance"
    assert 'boundary=' in content_type, "Expected boundary to be automatically included in Content-Type header"

def test_get_multipart_data_and_content_type_without_params(setup_data):
    mvod = {key: value for key, value in setup_data.items()}
    encoder, content_type = get_multipart_data_and_content_type(mvod)
    assert isinstance(encoder, MultipartEncoder), "Expected a MultipartEncoder instance"
    assert 'boundary=' in content_type, "Expected boundary to be automatically included in Content-Type header"