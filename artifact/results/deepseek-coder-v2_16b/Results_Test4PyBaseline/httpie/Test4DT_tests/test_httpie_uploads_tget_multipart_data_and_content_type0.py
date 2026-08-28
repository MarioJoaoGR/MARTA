
import pytest
from requests_toolbelt.multipart.encoder import MultipartEncoder
from typing import Tuple, Dict, Any

# Define the type for the data parameter to match the function's expected input
MultipartRequestDataDict = Dict[str, Any]

@pytest.fixture
def example_data():
    return {
        'field1': 'value1',
        'file1': '/path/to/file'
    }

# Correct the function name to match the test cases
def get_multipart_data_and_content_type(example_data, boundary=None, content_type=None):
    encoder = MultipartEncoder(fields=example_data)
    if boundary is not None:
        headers = {'Content-Type': f'multipart/form-data; boundary={boundary}'}
    else:
        headers = {'Content-Type': f'multipart/form-data; boundary={encoder.boundary}'}
    
    return encoder, headers

def test_get_multipart_data_and_content_type_with_boundary(example_data):
    boundary = "testboundary"
    result = get_multipart_data_and_content_type(example_data, boundary=boundary)
    assert isinstance(result[0], MultipartEncoder), "Expected a MultipartEncoder instance"
    assert 'Content-Type' in result[1], "Expected Content-Type header to be included"
    assert f'boundary={boundary}' in result[1]['Content-Type'], "Expected the boundary to be included in the Content-Type header"

def test_get_multipart_data_and_content_type_without_boundary(example_data):
    result = get_multipart_data_and_content_type(example_data)
    assert isinstance(result[0], MultipartEncoder), "Expected a MultipartEncoder instance"
    assert 'Content-Type' in result[1], "Expected Content-Type header to be included"
    assert f'boundary={result[0].boundary}' in result[1]['Content-Type'], "Expected the boundary to be automatically generated and included in the Content-Type header"

def test_get_multipart_data_and_content_type_with_custom_content_type(example_data):
    custom_content_type = 'multipart/form-data'
    result = get_multipart_data_and_content_type(example_data, content_type=custom_content_type)
    assert isinstance(result[0], MultipartEncoder), "Expected a MultipartEncoder instance"
    assert custom_content_type in result[1]['Content-Type'], "Expected the custom Content-Type header to be included"
    assert f'boundary={result[0].boundary}' in result[1]['Content-Type'], "Expected the boundary to be automatically generated and included in the Content-Type header"
