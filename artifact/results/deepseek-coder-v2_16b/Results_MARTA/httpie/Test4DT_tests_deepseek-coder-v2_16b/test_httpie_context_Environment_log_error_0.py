
import pytest
from httpie.context import Environment
import sys


def test_invalid_inputs():
    # Attempt to create an Environment with a non-existent file for stdin
    try:
        env = Environment(stdin='non-existent-file', stdout=sys.stdout, stderr=sys.stderr)
    except FileNotFoundError as e:
        pytest.fail("Expected an exception for invalid stdin file")