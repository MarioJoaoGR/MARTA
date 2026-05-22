
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

# Test case for invalid input
def test_invalid_input():
    with mock.patch('httpie.models.RequestsMessage', spec=True):
        # Create an instance of RequestsMessage that is not a PreparedRequest or Response
        class FakeMessage:
            pass
        
        fake_message = FakeMessage()
        
        try:
            infer_requests_message_kind(fake_message)
            assert False, "Expected TypeError was not raised"
        except TypeError as e:
            assert str(e) == "Unexpected message type: FakeMessage", f"Unexpected error message: {str(e)}"
