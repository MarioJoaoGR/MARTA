
import pytest
from sanic import Sanic
from sanic.response import text

# Define the function to be tested
def has_message_body(status):
    """
    Determines whether a message body should be included in the response based on the given HTTP status code.
    
    According to RFC 2616, message bodies SHOULD NOT be included in responses with status codes 1XX, 204, and 304. This function checks if the status is not 204 or any value between 100 and 199 (inclusive).
    
    Parameters:
        status (int): The HTTP status code to check.
        
    Returns:
        bool: True if the status is not in (204, 304) and not within the range 100 <= status < 200, False otherwise.
    
    Examples:
        >>> has_message_body(200)  # Should return True because 200 does not have a message body
        True
        
        >>> has_message_body(204)  # Should return False because status 204 should not have a message body
        False
        
        >>> has_message_body(105)  # Should return False because status 105 is in the range 100 <= status < 200
        False
    """
    return status not in (204, 304) and not (100 <= status < 200)

# Test cases for has_message_body function
def test_has_message_body_true():
    assert has_message_body(200) == True

def test_has_message_body_false_for_204():
    assert has_message_body(204) == False

def test_has_message_body_false_in_range_100_to_199():
    assert has_message_body(105) == False
