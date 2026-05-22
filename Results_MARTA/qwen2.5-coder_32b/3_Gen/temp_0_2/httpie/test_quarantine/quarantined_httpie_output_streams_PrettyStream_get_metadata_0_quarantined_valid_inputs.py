
import unittest
from unittest.mock import patch, MagicMock
from httpie.output.streams import PrettyStream
from conversion_class import Conversion
from formatting_class import Formatting

class TestPrettyStream(unittest.TestCase):
    def setUp(self):
        self.conversion = Conversion()
        self.formatting = Formatting()
        self.stream = PrettyStream(self.conversion, self.formatting)
        self.stream.output_encoding = 'utf-8'  # Assuming a default encoding for the test

    @patch('httpie.output.streams.PrettyStream.msg', new_callable=MagicMock)
    def test_get_metadata(self, mock_msg):
        mock_msg.metadata = MagicMock()
        mock_msg.metadata.return_value = "mock metadata"
        
        expected_output = self.formatting.format_metadata("mock metadata").encode('utf-8')
        result = self.stream.get_metadata()
        self.assertEqual(result, expected_output)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_streams_PrettyStream_get_metadata_0_test_valid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_streams_PrettyStream_get_metadata_0_test_valid_inputs.py:5:0: E0401: Unable to import 'conversion_class' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_streams_PrettyStream_get_metadata_0_test_valid_inputs.py:6:0: E0401: Unable to import 'formatting_class' (import-error)


"""