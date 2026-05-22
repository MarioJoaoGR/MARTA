
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import OutputOptions, RequestsMessageKind
from requests import PreparedRequest, Response

class TestOutputOptionsFromMessage:
    def test_valid_inputs(self):
        class RequestsMessage: pass  # Mocking the RequestsMessage class
    
        OPTION_TO_PARAM = {
            RequestsMessageKind.REQUEST: {'headers': 'h', 'body': 'b'},
            RequestsMessageKind.RESPONSE: {'headers': 'h', 'body': 'b'}
        }
    
        def infer_requests_message_kind(message: RequestsMessage) -> RequestsMessageKind:
            if isinstance(message, PreparedRequest):
                return RequestsMessageKind.REQUEST
            elif isinstance(message, Response):
                return RequestsMessageKind.RESPONSE
            else:
                raise TypeError("Unexpected message type")
    
        @patch('httpie.models.OutputOptions.from_message', side_effect=lambda cls, *args, **kwargs: OutputOptions(*args, **kwargs))
        def test_valid_inputs(self, mock_from_message):
            request = PreparedRequest()
            response = Response()
    
            output_options = OutputOptions.from_message(response)
    
            assert isinstance(output_options, OutputOptions)
            assert output_options.headers is False
            assert output_options.body is False
            assert output_options.meta is False

if __name__ == "__main__":
    pytest.main()
