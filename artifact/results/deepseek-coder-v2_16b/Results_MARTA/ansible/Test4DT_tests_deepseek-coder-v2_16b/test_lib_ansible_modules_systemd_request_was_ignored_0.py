
import pytest

def request_was_ignored(out):
    return '=' not in out and ('ignoring request' in out or 'ignoring command' in out)

# Test cases for different scenarios
@pytest.mark.parametrize("test_input, expected", [
    ("Output from a program: ignoring request due to invalid input", True),
    ("Another output: ignoring command - please check your inputs", True),
    ("Error message: = Unable to process the request", False),
    ("This is a test message", False)
])
def test_request_was_ignored(test_input, expected):
    assert request_was_ignored(test_input) == expected
