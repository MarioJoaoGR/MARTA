
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.writer import write_raw_data
from httpie.models import Environment, ProcessingOptions, HTTPHeadersDict

@pytest.fixture
def mock_environment():
    env = MagicMock(spec=Environment)
    return env

@pytest.fixture
def mock_processing_options():
    opts = MagicMock(spec=ProcessingOptions)
    return opts

@pytest.fixture
def mock_http_headers():
    headers = MagicMock(spec=HTTPHeadersDict)
    return headers

@patch('httpie.output.writer.requests')
@patch('httpie.output.writer.OutputOptions')
@patch('httpie.output.writer.write_message')
def test_write_raw_data(mock_write_message, mock_output_options, mock_requests):
    env = mock_environment()
    data = b'test data'
    headers = mock_http_headers()
    processing_options = mock_processing_options()
    
    with patch('httpie.output.writer.requests.PreparedRequest', autospec=True) as mock_request:
        mock_request.return_value.is_body_upload_chunk = True
        mock_request.return_value.body = data
        mock_request.return_value.headers = headers
        
        write_raw_data(env, data, processing_options=processing_options, headers=headers)
        
        mock_requests.PreparedRequest.assert_called_once()
        mock_output_options.from_message.assert_called_once_with(mock_request.return_value, body=True, headers=False)
        mock_write_message.assert_called_once_with(
            requests_message=mock_request.return_value,
            env=env,
            output_options=mock_output_options.return_value,
            processing_options=processing_options,
            extra_stream_kwargs={}
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_writer_write_raw_data_0_test_invalid_inputs
httpie/Test4DT_tests_codestral/test_httpie_output_writer_write_raw_data_0_test_invalid_inputs.py:5:0: E0611: No name 'Environment' in module 'httpie.models' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_writer_write_raw_data_0_test_invalid_inputs.py:5:0: E0611: No name 'ProcessingOptions' in module 'httpie.models' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_writer_write_raw_data_0_test_invalid_inputs.py:5:0: E0611: No name 'HTTPHeadersDict' in module 'httpie.models' (no-name-in-module)


"""