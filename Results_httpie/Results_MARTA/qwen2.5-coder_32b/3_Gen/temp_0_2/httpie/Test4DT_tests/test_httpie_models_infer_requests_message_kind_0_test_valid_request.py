
import unittest
from unittest.mock import patch
from httpie.models import RequestsMessage, RequestsMessageKind
import requests

class TestHttpieModelsInferRequestsMessageKind(unittest.TestCase):
    @patch('httpie.models.requests', autospec=True)
    def test_valid_request(self, mock_requests):
        # Arrange
        request = requests.PreparedRequest()
        response = requests.Response()
        
        # Act & Assert
        self.assertEqual(infer_requests_message_kind(request), RequestsMessageKind.REQUEST)
        self.assertEqual(infer_requests_message_kind(response), RequestsMessageKind.RESPONSE)

def infer_requests_message_kind(message: RequestsMessage) -> RequestsMessageKind:
    if isinstance(message, requests.PreparedRequest):
        return RequestsMessageKind.REQUEST
    elif isinstance(message, requests.Response):
        return RequestsMessageKind.RESPONSE
    else:
        raise TypeError(f"Unexpected message type: {type(message).__name__}")
