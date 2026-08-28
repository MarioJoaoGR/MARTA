
import pytest
from sanic import response
from typing import Dict, Optional

# Assuming the module and HTTPResponse class are correctly imported

def test_raw_default_content_type():
    # Arrange
    expected_body = b"Hello, World!"
    
    # Act
    response_obj = response.raw(body=expected_body)
    
    # Assert
    assert isinstance(response_obj, response.HTTPResponse), "Expected an instance of HTTPResponse"