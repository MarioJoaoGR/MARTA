
import pytest
from ansible.modules.systemd import request_was_ignored

# Test case 1: Output contains '=', so it should return False
def test_output_contains_equals():
    out = "Error message: = Unable to process the request"
    result = request_was_ignored(out)
    assert not result, f"Expected False for output '{out}', but got True."

# Test case 2: Output does not contain '=' and contains 'ignoring request'
def test_output_no_equals_contains_request():
    out = "Output from a program: ignoring request due to invalid input"
    result = request_was_ignored(out)
    assert result, f"Expected True for output '{out}', but got False."

# Test case 3: Output does not contain '=' and contains 'ignoring command'
def test_output_no_equals_contains_command():
    out = "Another output: ignoring command - please check your inputs"
    result = request_was_ignored(out)
    assert result, f"Expected True for output '{out}', but got False."

# Test case 4: Short string that does not meet the criteria for ignoring a request
def test_short_string():
    out = "This is a test message"
    result = request_was_ignored(out)
    assert not result, f"Expected False for output '{out}', but got True."
