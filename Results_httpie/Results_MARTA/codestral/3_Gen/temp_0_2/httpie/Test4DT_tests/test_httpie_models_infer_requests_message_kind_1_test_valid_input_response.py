
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
        # Mocking the requests.PreparedRequest and requests.Response objects
        request = mock.Mock(spec=requests.PreparedRequest)
        response = mock.Mock(spec=requests.Response)
        
        # Setting up the side effect to return specific RequestsMessageKind values
        mock_infer.side_effect = lambda message: {
            requests.PreparedRequest: RequestsMessageKind.REQUEST,
            requests.Response: RequestsMessageKind.RESPONSE
        }.get(type(message), TypeError)
        
        # Testing the function with a PreparedRequest instance
        assert infer_requests_message_kind(request) == RequestsMessageKind.REQUEST
        
        # Testing the function with a Response instance
        assert infer_requests_message_kind(response) == RequestsMessageKind.RESPONSE
        
        # Testing the function with an unexpected type to raise TypeError
        class UnexpectedType: pass
        try:
            infer_requests_message_kind(UnexpectedType())
        except TypeError as e:
            assert str(e) == "Unexpected message type: UnexpectedType"
