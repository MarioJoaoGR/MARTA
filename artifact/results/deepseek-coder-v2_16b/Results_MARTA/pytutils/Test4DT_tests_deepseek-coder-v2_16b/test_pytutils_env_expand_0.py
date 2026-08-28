
import pytest
from pytutils.env import expand
import os

def test_expand_with_environment_variable():
    # Assuming no environment variable is set for LOG_LEVEL, we expect the placeholder to remain unchanged
    result = expand("Hello ${LOG_LEVEL}")
    assert result == "Hello ${LOG_LEVEL}"


def test_expand_environment_variable():
    # Expanding a string containing an environment variable placeholder
    os.environ['LOG_LEVEL'] = 'debug'  # Mocking the environment variable for this test
    result = expand("Hello ${LOG_LEVEL}")
    assert result == "Hello debug"