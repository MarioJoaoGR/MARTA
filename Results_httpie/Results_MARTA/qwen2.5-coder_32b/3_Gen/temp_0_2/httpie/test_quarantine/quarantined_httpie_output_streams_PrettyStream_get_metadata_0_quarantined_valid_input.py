
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.streams import PrettyStream
from conversion_class import Conversion
from formatting_class import Formatting

@pytest.fixture
def setup_pretty_stream():
    conversion = Conversion()
    formatting = Formatting()
    stream = PrettyStream(conversion, formatting)
    return stream

def test_get_metadata(setup_pretty_stream):
    with patch('httpie.output.streams.PrettyStream.formatting') as mock_formatting:
        with patch('httpie.output.streams.PrettyStream.msg') as mock_msg:
            # Mocking the metadata and output_encoding attributes
            mock_msg.metadata = MagicMock()
            setup_pretty_stream.output_encoding = 'utf-8'
            
            # Mocking the format_metadata method of formatting class
            mock_formatting.format_metadata.return_value = "mocked_formatted_metadata"
            
            result = setup_pretty_stream.get_metadata()
            
            assert isinstance(result, bytes)
            mock_formatting.format_metadata.assert_called_once_with(mock_msg.metadata)
            assert result == b'mocked_formatted_metadata'.encode('utf-8')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_streams_PrettyStream_get_metadata_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_streams_PrettyStream_get_metadata_0_test_valid_input.py:5:0: E0401: Unable to import 'conversion_class' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_streams_PrettyStream_get_metadata_0_test_valid_input.py:6:0: E0401: Unable to import 'formatting_class' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_streams_PrettyStream_get_metadata_0_test_valid_input.py:29:29: E1101: Instance of 'bytes' has no 'encode' member (no-member)


"""