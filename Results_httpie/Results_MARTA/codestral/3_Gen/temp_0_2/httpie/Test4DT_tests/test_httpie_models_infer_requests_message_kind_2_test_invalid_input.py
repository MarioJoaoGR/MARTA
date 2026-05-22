
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
    with mock.patch('httpie.models.RequestsMessage', requests.PreparedRequest):
        # Create an instance of a non-supported type to simulate invalid input
        invalid_message = "Invalid message"
        
        try:
            infer_requests_message_kind(invalid_message)
        except TypeError as e:
            assert str(e) == "Unexpected message type: str"
