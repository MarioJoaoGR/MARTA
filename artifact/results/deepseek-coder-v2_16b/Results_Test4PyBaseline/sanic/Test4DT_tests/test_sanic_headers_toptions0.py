# Module: sanic.headers
import pytest
from sanic.headers import options

# Test cases for the options function
def test_options():
    # Define a sample header dictionary
    headers = {
        "x-scheme": "https",
        "x-forwarded-proto": "http",  # This should override the x-scheme value
        "x-forwarded-host": "example.com",
        "x-forwarded-port": "80",
        "x-forwarded-path": "/test"
    }
    
    expected_output = [
        ("proto", "http"),  # Should be overridden by x-forwarded-proto
        ("host", "example.com"),
        ("port", "80"),
        ("path", "/test")
    ]
    
    result = list(options())
    assert result == expected_output
