
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.streams import PrettyStream
from conversion_class import Conversion
from formatting_class import Formatting

@pytest.fixture
def setup_pretty_stream():
    conversion = Conversion()
    formatting = Formatting()
    return PrettyStream(conversion=conversion, formatting=formatting)

def test_iter_body_edge_case(setup_pretty_stream):
    stream = setup_pretty_stream
    # Mocking the message object to simulate a chunked response with null bytes
    mock_msg = MagicMock()
    mock_msg.iter_lines = lambda x: [b'line1\0', b'line2', b'\n']  # Simulating iter_lines output
    stream.msg = mock_msg
    
    # Mocking the conversion and formatting classes to simulate successful conversion and processing
    with patch('conversion_class.Conversion') as mock_conversion, \
         patch('formatting_class.Formatting') as mock_formatting:
        mock_converter = MagicMock()
        mock_converter.convert.return_value = (stream.mime, b'processed_body'.decode())
        mock_conversion.get_converter.return_value = mock_converter
        
        with pytest.raises(BinarySuppressedError):
            list(stream.iter_body())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_streams_PrettyStream_iter_body_0_test_edge_case
httpie/Test4DT_tests_codestral/test_httpie_output_streams_PrettyStream_iter_body_0_test_edge_case.py:5:0: E0401: Unable to import 'conversion_class' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_streams_PrettyStream_iter_body_0_test_edge_case.py:6:0: E0401: Unable to import 'formatting_class' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_streams_PrettyStream_iter_body_0_test_edge_case.py:28:27: E0602: Undefined variable 'BinarySuppressedError' (undefined-variable)


"""