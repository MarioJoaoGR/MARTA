
import pytest
from sanic.response import HTTPResponse
from typing import Dict, Optional

def empty(status=204, headers: Optional[Dict[str, str]] = None) -> HTTPResponse:
    """
    Returns an empty response to the client with a specified status code and optional custom headers.
    
    This function creates an HTTPResponse object with no body content, using the provided status code (defaulting to 204 No Content if not specified) and optional custom headers. The resulting response can be used to inform clients that the request was successfully handled but there is no additional information to send back.
    
    Parameters:
        status (int): The HTTP status code for the response. Default is 204, indicating a successful handling of the request with no content to send back.
        headers (Optional[Dict[str, str]]): A dictionary containing custom HTTP headers to be included in the response. If not provided, defaults to an empty dictionary.
        
    Returns:
        HTTPResponse: An instance of the HTTPResponse class representing the empty response.
    
    Examples:
        >>> response = empty()
        >>> print(response.status)  # Outputs: 204
        >>> print(response.headers)  # Outputs: {}
        >>> print(response.body)      # Outputs: b''
        
        >>> custom_headers = {"X-Custom-Header": "value"}
        >>> response = empty(status=200, headers=custom_headers)
        >>> print(response.status)  # Outputs: 200
        >>> print(response.headers)  # Outputs: {'X-Custom-Header': 'value'}
        >>> print(response.body)      # Outputs: b''
    """
    return HTTPResponse(body=b"", status=status, headers=headers)

def test_default_empty_response():
    response = empty()
    assert response.status == 204
    assert response.headers == {}
    assert response.body == b''

def test_custom_empty_response():
    custom_headers = {"X-Custom-Header": "value"}
    response = empty(status=200, headers=custom_headers)
    assert response.status == 200
    assert response.headers == custom_headers
    assert response.body == b''
