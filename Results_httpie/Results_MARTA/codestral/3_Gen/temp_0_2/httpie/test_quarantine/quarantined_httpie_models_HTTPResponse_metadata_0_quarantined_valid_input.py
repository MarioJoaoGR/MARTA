
import pytest
from unittest.mock import patch
from httpie.models import HTTPResponse

def test_valid_input():
    # Create a mock response object with elapsed time for headers and body parsing times
    class MockResponse:
        def __init__(self):
            self.elapsed = 1.2345678901  # Total elapsed time in seconds
            self._httpie_headers_parsed_at = 0.1234567890  # Time when headers were parsed
        
        @property
        def _orig(self):
            return self
    
    mock_response = MockResponse()
    http_response = HTTPResponse(mock_response)
    
    with patch('httpie.models.monotonic', return_value=1234567890.123456):
        metadata_str = http_response.metadata()
        
        assert "Headers time: 1.2345678901s" in metadata_str
        assert "Body time: 1098765432.0s" in metadata_str
        assert "Total elapsed time: 1098765432.123456s" in metadata_str

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_models_HTTPResponse_metadata_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_models_HTTPResponse_metadata_0_test_valid_input.py:21:23: E1102: http_response.metadata is not callable (not-callable)


"""