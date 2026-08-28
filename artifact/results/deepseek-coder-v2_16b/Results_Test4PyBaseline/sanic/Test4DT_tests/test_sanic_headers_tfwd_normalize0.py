# Module: sanic.headers
import pytest
from typing import Dict, Union, List
from urllib.parse import unquote
from your_module_name import fwd_normalize  # Replace 'your_module_name' with the actual module name

# Define a sample OptionsIterable for testing
OptionsIterable = List[Dict[str, str]]

def test_fwd_normalize():
    # Test case 1: Normalizing Forwarded Headers
    forwarded_headers = {
        "by": "ExampleHost",
        "for": None,
        "host": "EXAMPLE.com",
        "proto": "HTTP/1.1",
        "port": "8080",
        "path": "https://example.org/page"
    }
    expected_output = {
        "by": "examplehost",
        "for": "",
        "host": "example.com",
        "proto": "http/1.1",
        "port": 8080,
        "path": "https://example.org/page"
    }
    assert fwd_normalize(forwarded_headers) == expected_output

def test_fwd_normalize_with_none():
    # Test case 2: Handling None Values
    forwarded_headers_with_none = {
        "by": "ExampleHost",
        "for": None,
        "host": "EXAMPLE.com",
        "proto": "HTTP/1.1",
        "port": None,
        "path": "https://example.org/page"
    }
    expected_output = {
        "by": "examplehost",
        "for": "",
        "host": "example.com",
        "proto": "http/1.1",
        "port": 8080,
        "path": "https://example.org/page"
    }
    assert fwd_normalize(forwarded_headers_with_none) == expected_output

def test_fwd_normalize_specific_headers():
    # Test case 3: Normalizing Specific Headers
    specific_headers = {
        "by": "ExampleHost",
        "for": "AnotherHost",
        "host": "EXAMPLE.com",
        "proto": "HTTP/1.1",
        "port": "8080",
        "path": "https://example.org/page"
    }
    expected_output = {
        "by": "examplehost",
        "for": "anotherhost",
        "host": "example.com",
        "proto": "http/1.1",
        "port": 8080,
        "path": "https://example.org/page"
    }
    assert fwd_normalize(specific_headers) == expected_output

def test_fwd_normalize_different_headers():
    # Test case 4: Handling Different Header Types
    different_headers = {
        "by": "ExampleHost",
        "for": "AnotherHost",
        "host": "EXAMPLE.com",
        "proto": "HTTP/1.1",
        "port": "8080",
        "path": "https://example.org/page"
    }
    expected_output = {
        "by": "examplehost",
        "for": "anotherhost",
        "host": "example.com",
        "proto": "http/1.1",
        "port": 8080,
        "path": "https://example.org/page"
    }
    assert fwd_normalize(different_headers) == expected_output

# Add more test cases as needed to cover different scenarios and edge cases
