
import unittest
from unittest.mock import patch, MagicMock
from httpie.output.streams import PrettyStream
from conversion_class import Conversion
from formatting_class import Formatting

class TestPrettyStream(unittest.TestCase):
    @patch('httpie.output.streams.Formatting')
    @patch('httpie.output.streams.Conversion')
    def test_get_metadata(self, MockConversion, MockFormatting):
        # Arrange
        conversion = MockConversion()
        formatting = MockFormatting()
        pretty_stream = PrettyStream(conversion, formatting)
        pretty_stream.msg = MagicMock()
        pretty_stream.msg.metadata = b"test metadata"
        pretty_stream.output_encoding = "utf-8"
        expected_output = b"formatted test metadata"
        
        # Mock the format_metadata method to return a specific byte string
        formatting.format_metadata.return_value = expected_output
        
        # Act
        result = pretty_stream.get_metadata()
        
        # Assert
        self.assertEqual(result, expected_output)
        MockFormatting.assert_called_once_with()
        MockConversion.assert_called_once_with()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_streams_PrettyStream_get_metadata_0_test_edge_cases
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_PrettyStream_get_metadata_0_test_edge_cases.py:5:0: E0401: Unable to import 'conversion_class' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_PrettyStream_get_metadata_0_test_edge_cases.py:6:0: E0401: Unable to import 'formatting_class' (import-error)


"""