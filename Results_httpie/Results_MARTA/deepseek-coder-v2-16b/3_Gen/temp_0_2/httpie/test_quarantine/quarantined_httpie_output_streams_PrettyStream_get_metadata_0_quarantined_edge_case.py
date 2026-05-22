
import unittest
from unittest.mock import patch, MagicMock
from httpie.output.streams import PrettyStream
from conversion_class import Conversion
from formatting_class import Formatting

class TestPrettyStream(unittest.TestCase):
    @patch('httpie.output.streams.PrettyStream')
    def test_get_metadata(self, MockPrettyStream):
        # Create mock instances of Conversion and Formatting
        conversion = MagicMock()
        formatting = MagicMock()
        
        # Set up the mock PrettyStream instance
        pretty_stream = MockPrettyStream.return_value
        pretty_stream.conversion = conversion
        pretty_stream.formatting = formatting
        pretty_stream.output_encoding = 'UTF-8'  # Assuming default encoding is UTF-8
        
        # Create a mock metadata object
        metadata = MagicMock()
        pretty_stream.msg.metadata = metadata
        
        # Mock the format_metadata method of Formatting
        formatting.format_metadata.return_value = "formatted_metadata"
        
        # Call the get_metadata method
        result = pretty_stream.get_metadata()
        
        # Assert that the encoding is applied correctly
        self.assertEqual(result, b"formatted_metadata")
        formatting.format_metadata.assert_called_once_with(metadata)
        pretty_stream.conversion.encode.assert_called_once_with('UTF-8')

if __name__ == '__main__':
    unittest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_streams_PrettyStream_get_metadata_0_test_edge_case
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_PrettyStream_get_metadata_0_test_edge_case.py:5:0: E0401: Unable to import 'conversion_class' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_streams_PrettyStream_get_metadata_0_test_edge_case.py:6:0: E0401: Unable to import 'formatting_class' (import-error)


"""