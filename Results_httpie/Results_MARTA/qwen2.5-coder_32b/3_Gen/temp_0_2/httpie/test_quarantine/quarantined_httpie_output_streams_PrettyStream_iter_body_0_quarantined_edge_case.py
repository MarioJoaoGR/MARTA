
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

def test_iter_body_with_null_bytes(setup_pretty_stream):
    # Mock the message object to have a method `iter_lines` that yields chunks of data
    with patch.object(setup_pretty_stream.msg.__class__, 'iter_lines', return_value=[b'line1\0line2', b'line3']):
        setup_pretty_stream.mime = "text/plain"  # Mock the MIME type for testing
        converter_mock = MagicMock()
        converter_mock.convert.return_value = ("new_mime", "processed_body")
        with patch('conversion_class.Conversion.get_converter', return_value=converter_mock):
            with pytest.raises(BinarySuppressedError):
                list(setup_pretty_stream.iter_body())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_streams_PrettyStream_iter_body_0_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_streams_PrettyStream_iter_body_0_test_edge_case.py:5:0: E0401: Unable to import 'conversion_class' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_streams_PrettyStream_iter_body_0_test_edge_case.py:6:0: E0401: Unable to import 'formatting_class' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_streams_PrettyStream_iter_body_0_test_edge_case.py:21:31: E0602: Undefined variable 'BinarySuppressedError' (undefined-variable)


"""