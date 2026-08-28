
import pytest
from ansible.modules.systemd import request_was_ignored

# Test cases for the function documentation examples
def test_request_was_ignored_examples():
    assert not request_was_ignored("This is a test message")
    assert request_was_ignored("Output from a program: ignoring request due to some reason")
    assert request_was_ignored("Another output: ignoring command - please check the input")