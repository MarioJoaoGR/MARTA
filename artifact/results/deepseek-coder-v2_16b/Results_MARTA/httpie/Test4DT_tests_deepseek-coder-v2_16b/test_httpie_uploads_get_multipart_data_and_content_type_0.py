
import pytest
from httpie.uploads import get_multipart_data_and_content_type
from requests_toolbelt.multipart.encoder import MultipartEncoder
from collections import OrderedDict

# Define a dictionary with file paths and bytes-like objects for testing
data_dict = {
    'file1': '/path/to/file1',
    'file2': b'bytes_content_of_file2'
}

def test_get_multipart_data_and_content_type_default():
    mvod = OrderedDict(data_dict.items())
    encoder, content_type = get_multipart_data_and_content_type(mvod)
    assert isinstance(encoder, MultipartEncoder), "Expected a MultipartEncoder instance"
    assert 'boundary=' in content_type, "Expected the Content-Type to include boundary specification"

def test_get_multipart_data_and_content_type_with_boundary():
    mvod = OrderedDict(data_dict.items())
    encoder, content_type = get_multipart_data_and_content_type(mvod, boundary='boundary123')
    assert isinstance(encoder, MultipartEncoder), "Expected a MultipartEncoder instance"
    assert 'boundary=boundary123' in content_type, "Expected the Content-Type to include specified boundary"

def test_get_multipart_data_and_content_type_with_custom_content_type():
    mvod = OrderedDict(data_dict.items())
    encoder, content_type = get_multipart_data_and_content_type(mvod, content_type='multipart/form-data')
    assert isinstance(encoder, MultipartEncoder), "Expected a MultipartEncoder instance"
    assert 'boundary=' in content_type, "Expected the Content-Type to include boundary specification"
    assert content_type.startswith('multipart/form-data'), "Expected the Content-Type to start with 'multipart/form-data'"
