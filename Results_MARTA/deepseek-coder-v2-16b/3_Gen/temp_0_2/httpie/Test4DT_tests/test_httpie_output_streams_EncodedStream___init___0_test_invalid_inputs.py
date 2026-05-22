
import pytest
from unittest.mock import patch
from httpie.output.streams import EncodedStream, Environment, UTF8, parse_content_type_header

class TestEncodedStreamInit:
    @patch('httpie.output.streams.Environment')
    @patch('httpie.output.streams.parse_content_type_header')
    @patch('httpie.output.streams.UTF8')
    def test_invalid_inputs(self, MockUTF8, MockParseContentTypeHeader, MockEnvironment):
        # Arrange
        mock_env = MockEnvironment.return_value
        mock_parse_content_type_header = MockParseContentTypeHeader.return_value
        mock_utf8 = MockUTF8.return_value
        
        # Act & Assert
        with pytest.raises(TypeError):
            EncodedStream()  # Missing required arguments
        
        with pytest.raises(TypeError):
            EncodedStream(env=mock_env)  # Missing optional arguments
        
        with pytest.raises(TypeError):
            EncodedStream(mime_overwrite='text/plain')  # Missing env argument
        
        with pytest.raises(TypeError):
            EncodedStream(encoding_overwrite='utf-8')  # Missing env argument
        
        mock_env.stdout_isatty = False
        mock_env.stdout_encoding = 'ascii'
        with pytest.raises(TypeError):
            stream = EncodedStream(env=mock_env, mime_overwrite='text/plain', encoding_overwrite='utf-8')
