
import pytest
from httpie.models import HTTPMessage

class TestHTTPMessageInit:
    def test_valid_input(self):
        # Create a valid input for testing
        orig = {"key": "value"}
        
        # Instantiate the HTTPMessage class with the valid input
        http_message = HTTPMessage(orig)
        
        # Assert that the _orig attribute is correctly set
        assert hasattr(http_message, '_orig')
        assert http_message._orig == orig
