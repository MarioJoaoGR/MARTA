
import pytest
from ansible.modules.systemd import request_was_ignored

# Test cases for the function documentation examples
def test_request_was_ignored_examples():
    assert request_was_ignored("This is a test message") == False
    assert request_was_ignored("Output from a program: ignoring request due to some reason") == True
    assert request_was_ignored("Another output: ignoring command - please check the input") == True
    assert request_was_ignored("Error encountered: =404 Not Found") == False

# Edge cases to ensure robustness
def test_request_was_ignored_edge():
    # Empty string should return False as per function definition
    assert request_was_ignored("") == False
    
    # String with '=' but no 'ignoring' keywords should return False
    assert request_was_ignored("Output from a program: =404 Not Found") == False
    
    # String with only 'ignoring' keyword regardless of content should return True