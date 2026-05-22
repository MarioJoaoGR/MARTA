
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

def test_valid_input(setup_pretty_stream):
    stream = setup_pretty_stream
    
    # Mocking the iter_lines method to simulate a chunked response
    with patch.object(stream.msg, 'iter_lines', return_value=iter(['line1\n', 'line2\n'])):
        chunks = list(stream.iter_body())
        
        assert len(chunks) == 2
        assert chunks[0] == b'processed line1\n'
        assert chunks[1] == b'processed line2\n'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_streams_PrettyStream_iter_body_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_output_streams_PrettyStream_iter_body_0_test_valid_input.py:5:0: E0401: Unable to import 'conversion_class' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_streams_PrettyStream_iter_body_0_test_valid_input.py:6:0: E0401: Unable to import 'formatting_class' (import-error)


"""