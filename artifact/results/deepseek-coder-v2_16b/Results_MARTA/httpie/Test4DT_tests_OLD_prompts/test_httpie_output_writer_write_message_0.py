
import pytest
from httpie.context import Environment
import requests
import argparse
from unittest.mock import patch, MagicMock

def test_write_message_with_headers_and_body():
    env = Environment()
    args = argparse.Namespace(prettify=True, stream=True)
    requests_message = requests.PreparedRequest()  # Replace with actual request object if available
    
    with patch('httpie.output.writer.write_stream', autospec=True) as mock_write_stream:
        from httpie.output.writer import write_message
        write_message(requests_message, env, args, with_headers=True, with_body=True)
        
        assert mock_write_stream.call_count == 1

def test_write_message_with_headers_only():
    env = Environment()
    args = argparse.Namespace(prettify=False, stream=True)
    requests_message = requests.Response()  # Replace with actual response object if available
    
    with patch('httpie.output.writer.write_stream', autospec=True) as mock_write_stream:
        from httpie.output.writer import write_message
        write_message(requests_message, env, args, with_headers=True, with_body=False)
        
        assert mock_write_stream.call_count == 1

def test_write_message_without_headers_and_body():
    env = Environment()
    args = argparse.Namespace(prettify=False, stream=False)
    requests_message = requests.PreparedRequest()  # Replace with actual request object if available
    
    with patch('httpie.output.writer.write_stream', autospec=True) as mock_write_stream:
        from httpie.output.writer import write_message
        write_message(requests_message, env, args, with_headers=False, with_body=False)
        
        assert mock_write_stream.call_count == 0
