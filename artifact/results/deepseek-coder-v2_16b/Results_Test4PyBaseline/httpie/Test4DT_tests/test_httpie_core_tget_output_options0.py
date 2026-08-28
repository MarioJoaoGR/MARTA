# Module: httpie.core
import argparse
import pytest
import requests
from typing import Union, Tuple

# Assuming the function implementation is as provided above
def get_output_options(args: argparse.Namespace, message: Union[requests.PreparedRequest, requests.Response]) -> Tuple[bool, bool]:
    return {
        requests.PreparedRequest: (
            'headers' in args.output_options,
            'body' in args.output_options,
        ),
        requests.Response: (
            'headers' in args.output_options,
            'body' in args.output_options,
        ),
    }[type(message)]

# Test cases for get_output_options function
def test_get_output_options_request():
    # Arrange
    args = argparse.Namespace(output_options=['headers', 'body'])
    req = requests.PreparedRequest()
    
    # Act
    should_include_headers, should_include_body = get_output_options(args, req)
    
    # Assert
    assert should_include_headers is True
    assert should_include_body is True

def test_get_output_options_response():
    # Arrange
    args = argparse.Namespace(output_options=['headers'])
    resp = requests.Response()
    
    # Act
    should_include_headers, should_include_body = get_output_options(args, resp)
    
    # Assert
    assert should_include_headers is True
    assert should_include_body is False

def test_get_output_options_no_options():
    # Arrange
    args = argparse.Namespace(output_options=[])
    req = requests.PreparedRequest()
    
    # Act
    should_include_headers, should_include_body = get_output_options(args, req)
    
    # Assert
    assert should_include_headers is False
    assert should_include_body is False

def test_get_output_options_invalid_type():
    # Arrange
    args = argparse.Namespace(output_options=['headers'])
    with pytest.raises(KeyError):  # Assuming the function raises KeyError for invalid message type
        get_output_options(args, "invalid_message")
