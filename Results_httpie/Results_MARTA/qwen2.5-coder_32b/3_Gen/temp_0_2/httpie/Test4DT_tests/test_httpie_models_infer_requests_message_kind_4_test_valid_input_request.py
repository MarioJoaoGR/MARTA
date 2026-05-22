
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

# Test case for valid input request
def test_valid_input_request():
    with mock.patch('httpie.models.RequestsMessage', requests.PreparedRequest):
        request = requests.PreparedRequest()
        assert infer_requests_message_kind(request) == RequestsMessageKind.REQUEST
