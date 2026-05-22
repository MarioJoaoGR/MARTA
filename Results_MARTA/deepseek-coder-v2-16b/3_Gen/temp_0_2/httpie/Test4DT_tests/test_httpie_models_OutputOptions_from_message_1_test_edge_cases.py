
import unittest
from unittest.mock import patch
from httpie.models import RequestsMessageKind, OutputOptions

# Assuming the following definitions for RequestsMessage and OPTION_TO_PARAM
class RequestsMessage:
    pass

class PreparedRequest(RequestsMessage):
    pass

class Response(RequestsMessage):
    pass

OPTION_TO_PARAM = {
    RequestsMessageKind.REQUEST: {'headers': 'h', 'body': 'b'},
    RequestsMessageKind.RESPONSE: {'headers': 'h', 'body': 'b'}
}

class TestOutputOptionsFromMessage(unittest.TestCase):
    
    @patch('httpie.models.infer_requests_message_kind')
    def test_from_message_default(self, mock_infer):
        # Mock the return value of infer_requests_message_kind
        mock_infer.return_value = RequestsMessageKind.RESPONSE
        
        response = Response()
        output_options = OutputOptions.from_message(response)
        
        self.assertEqual(output_options.headers, False)
        self.assertEqual(output_options.body, False)
        self.assertEqual(output_options.meta, False)
    
    @patch('httpie.models.infer_requests_message_kind')
    def test_from_message_with_args(self, mock_infer):
        # Mock the return value of infer_requests_message_kind
        mock_infer.return_value = RequestsMessageKind.REQUEST
        
        request = PreparedRequest()
        output_options = OutputOptions.from_message(request, headers=True, body=True)
        
        self.assertEqual(output_options.headers, True)
        self.assertEqual(output_options.body, True)
        self.assertEqual(output_options.meta, False)

if __name__ == '__main__':
    unittest.main()
