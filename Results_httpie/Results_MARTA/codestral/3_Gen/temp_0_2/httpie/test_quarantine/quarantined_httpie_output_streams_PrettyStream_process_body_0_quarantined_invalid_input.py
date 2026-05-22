
from unittest.mock import patch, MagicMock
import pytest
from httpie.output.streams import pretty_stream  # Adjusted import to match module path

@pytest.fixture(autouse=True)
def mock_pretty_stream():
    with patch('httpie.output.streams.pretty_stream', autospec=True):
        yield

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_streams_PrettyStream_process_body_0_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_output_streams_PrettyStream_process_body_0_test_invalid_input.py:4:0: E0611: No name 'pretty_stream' in module 'httpie.output.streams' (no-name-in-module)


"""