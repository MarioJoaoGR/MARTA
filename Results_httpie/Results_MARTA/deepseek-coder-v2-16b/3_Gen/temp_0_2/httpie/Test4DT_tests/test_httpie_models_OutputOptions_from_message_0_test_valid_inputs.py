
import unittest
from unittest.mock import patch, MagicMock
from httpie.models import RequestsMessageKind, OutputOptions, OPTION_TO_PARAM

class TestOutputOptionsFromMessage(unittest.TestCase):
    @patch('httpie.models.infer_requests_message_kind', return_value=RequestsMessageKind.RESPONSE)
    def test_valid_inputs(self, mock_infer):
        response = MagicMock()
        output_options = OutputOptions.from_message(response)
        self.assertEqual(output_options.headers, False)
        self.assertEqual(output_options.body, False)
        self.assertEqual(output_options.meta, False)

    @patch('httpie.models.infer_requests_message_kind', return_value=RequestsMessageKind.REQUEST)
    def test_valid_inputs_with_args(self, mock_infer):
        request = MagicMock()
        output_options = OutputOptions.from_message(request, headers=True, body=True)
        self.assertEqual(output_options.headers, True)
        self.assertEqual(output_options.body, True)
        self.assertEqual(output_options.meta, False)
