
import pytest
from tornado.simple_httpclient import HTTPStreamClosedError

def test_HTTPStreamClosedError_str():
    # Arrange
    error = HTTPStreamClosedError("Test message")
    
    # Act and Assert
    assert str(error) == "Test message"
