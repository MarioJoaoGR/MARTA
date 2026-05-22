
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
def test_valid_input_response():
    with mock.patch('httpie.models.infer_requests_message_kind') as mock_infer:
        # Mocking requests.PreparedRequest and requests.Response
        request = mock.Mock(spec=requests.PreparedRequest)
        response = mock.Mock(spec=requests.Response)
        
        # Setting return value for the mocked function
        mock_infer.return_value = RequestsMessageKind.REQUEST
        
        # Calling the function with a valid request
        result = infer_requests_message_kind(request)
        
        # Asserting the expected outcome
        assert result == RequestsMessageKind.REQUEST
        
        # Resetting the mock to ensure no side effects in subsequent tests
        mock_infer.reset_mock()
        
        # Setting return value for the mocked function
        mock_infer.return_value = RequestsMessageKind.RESPONSE
        
        # Calling the function with a valid response
        result = infer_requests_message_kind(response)
        
        # Asserting the expected outcome
        assert result == RequestsMessageKind.RESPONSE
