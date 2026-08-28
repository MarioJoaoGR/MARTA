
import pytest
from unittest.mock import patch, MagicMock
from sanic.response import raw, HTTPResponse
from typing import Optional, Dict, AnyStr

# Define the function to be tested
def raw(
    body: Optional[AnyStr],
    status: int = 200,
    headers: Optional[Dict[str, str]] = None,
    content_type: str = 'text/html'
) -> HTTPResponse:
    """
    Returns a raw HTTP response object without encoding the body.
    
    This function creates an `HTTPResponse` instance with the provided parameters. The body is passed as-is without any additional processing or encoding. The status code, headers, and content type can be customized according to the user's requirements.
    
    Parameters:
        body (Optional[AnyStr]): The response data which could be bytes or str. If a string is provided, it will be encoded to bytes using UTF-8 by default before being included in the HTTPResponse object.
        status (int): The HTTP status code for the response. Default is 200.
        headers (Optional[Dict[str, str]]): A dictionary containing custom HTTP headers. If not provided, defaults to an empty dictionary.
        content_type (str): Specifies the MIME type of the body content. Default is DEFAULT_HTTP_CONTENT_TYPE which could be 'text/html', 'application/json', etc., depending on the use case.
        
    Returns:
        HTTPResponse: An instance of the `HTTPResponse` class initialized with the provided parameters.
    """
    return HTTPResponse(
        body=body,
        status=status,
        headers=headers,
        content_type=content_type
    )

# Test cases for edge cases and invalid inputs

def test_invalid_inputs():
    with pytest.raises(TypeError):
        raw()