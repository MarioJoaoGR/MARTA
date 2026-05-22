
import unittest.mock as mock
from httpie.models import RequestsMessage, RequestsMessageKind
import requests

def infer_requests_message_kind(message: RequestsMessage) -> RequestsMessageKind:
    if isinstance(message, requests.PreparedRequest):
        return RequestsMessageKind.REQUEST
    elif isinstance(message, requests.Response):
        return RequestsMessageKind.RESPONSE
    else:
        raise TypeError(f"Unexpected message type: {type(message).__name__}")

# Test case for infer_requests_message_kind function
def test_valid_input_request():
    with mock.patch('httpie.models.infer_requests_message_kind') as mock_infer:
        # Mocking the requests.PreparedRequest and requests.Response objects
        request = mock.Mock(spec=requests.PreparedRequest)
        response = mock.Mock(spec=requests.Response)
        
        # Setting up the return values for the mocked function
        mock_infer.return_value = RequestsMessageKind.REQUEST
        
        # Calling the function with a valid request object
        result = infer_requests_message_kind(request)
        
        # Asserting that the function returned the expected value
        assert result == RequestsMessageKind.REQUEST
