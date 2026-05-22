
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import RequestItems, RequestType, KeyValueArg

@pytest.fixture
def valid_request():
    return RequestItems(request_type=RequestType.JSON)

def test_valid_inputs(valid_request):
    assert isinstance(valid_request, RequestItems)
    assert valid_request.headers is not None
    assert valid_request.is_json is True
    assert isinstance(valid_request.data, dict)  # Assuming JSON data is a dictionary
    assert valid_request.files == {}
    assert valid_request.params == {}
    assert isinstance(valid_request.multipart_data, dict)
