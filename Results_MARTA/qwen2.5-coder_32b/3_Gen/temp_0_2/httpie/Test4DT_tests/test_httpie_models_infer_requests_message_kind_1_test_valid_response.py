
import unittest
from unittest.mock import patch
from httpie.models import RequestsMessage, RequestsMessageKind
import requests

class TestInferRequestsMessageKind(unittest.TestCase):
    @patch('httpie.models.requests', requests)  # Mock the requests module
    def test_valid_response(self):
        request = requests.PreparedRequest()
        response = requests.Response()
        
        self.assertEqual(infer_requests_message_kind(request), RequestsMessageKind.REQUEST)
        self.assertEqual(infer_requests_message_kind(response), RequestsMessageKind.RESPONSE)

def infer_requests_message_kind(message: RequestsMessage) -> RequestsMessageKind:
    if isinstance(message, requests.PreparedRequest):
        return RequestsMessageKind.REQUEST
    elif isinstance(message, requests.Response):
        return RequestsMessageKind.RESPONSE
    else:
        raise TypeError(f"Unexpected message type: {type(message).__name__}")
