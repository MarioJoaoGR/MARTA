
import pytest

def unquote(data):
    ''' removes first and last quotes from a string, if the string starts and ends with the same quotes '''
    if is_quoted(data):
        return data[1:-1]
    return data

def is_quoted(data):
    """Helper function to check if a string is quoted."""
    if len(data) >= 2:
        if (data[0] == '"' and data[-1] == '"') or (data[0] == "'" and data[-1] == "'"):
            return True
    return False

# Test function for unquote with basic functionality
def test_unquote_basic():
    # Example 1: No change since the string is not enclosed in quotes
    assert unquote("Hello, World!") == "Hello, World!"
    
    # Example 2: No change since the string is not enclosed in quotes
    assert unquote('Hello, World!') == 'Hello, World!'
    
    # Example 3: The string is enclosed in double quotes, so the surrounding quotes are removed
    assert unquote("\"Hello, World!\"") == "Hello, World!"
    
    # Example 4: The string is enclosed in single quotes, so the surrounding quotes are removed
    assert unquote('\'Hello, World!\'') == 'Hello, World!'
