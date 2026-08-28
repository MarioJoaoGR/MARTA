
import pytest
from ansible.plugins.filter import urls

# Test cases for urldecode filter
def test_urldecode():
    # Test case 1: Decoding a simple URL-encoded string
    encoded_string = "https%3A%2F%2Fexample.com"
    expected_output = "https://example.com"
    assert urls.FilterModule().filters()['urldecode'](encoded_string) == expected_output, f"Expected '{expected_output}' but got '{urls.FilterModule().filters()['urldecode'](encoded_string)}'"

    # Test case 2: Decoding a string with special characters
    encoded_string = "http%3A%2F%2Fexample.com%2Fpath%3Fquery%3Dvalue"
    expected_output = "http://example.com/path?query=value"
    assert urls.FilterModule().filters()['urldecode'](encoded_string) == expected_output, f"Expected '{expected_output}' but got '{urls.FilterModule().filters()['urldecode'](encoded_string)}'"

    # Test case 3: Decoding an already decoded string (should remain unchanged)
    encoded_string = "https%3A%2F%2Fexample.com"