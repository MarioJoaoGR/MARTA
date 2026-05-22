
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPMessage

def test_iter_body():
    # Create a mock HTTPMessage instance
    with patch('httpie.models.HTTPMessage') as MockHTTPMessage:
        # Create an iterable object to simulate the body content
        class IterableMock:
            def __init__(self, data):
                self.data = data
            
            def __iter__(self):
                return iter(self.data)
        
        # Configure the mock to return the iterable mock when iter_body is called
        instance = MockHTTPMessage.return_value
        instance.iter_body = MagicMock(return_value=IterableMock([b'chunk1', b'chunk2']))
        
        # Call the method under test
        result = list(instance.iter_body(chunk_size=8))
        
        # Assert that the result is as expected
        assert result == [b'chunk1', b'chunk2']
