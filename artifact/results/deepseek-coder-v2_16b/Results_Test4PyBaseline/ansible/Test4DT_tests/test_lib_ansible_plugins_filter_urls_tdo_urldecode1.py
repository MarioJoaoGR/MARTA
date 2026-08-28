
import pytest
from ansible.plugins.filter.urls import do_urldecode

# Test cases for Python 3 (ASCII input)
def test_do_urldecode_python3():
    assert do_urldecode("Hello%20World") == "Hello World"
    # Additional test case to check decoding of a string with multiple encoded parts
    assert do_urldecode("This%20is%20a%20test") == "This is a test"
    # Test case for an empty string
    assert do_urldecode("") == ""
    # Test case for a string without any encoding