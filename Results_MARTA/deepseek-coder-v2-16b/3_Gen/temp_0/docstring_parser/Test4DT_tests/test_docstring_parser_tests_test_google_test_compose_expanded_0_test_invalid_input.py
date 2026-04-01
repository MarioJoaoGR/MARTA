
import pytest
from docstring_parser.tests.test_google import test_compose_expanded, parse, compose, RenderingStyle

def test_invalid_input():
    with pytest.raises(AssertionError):
        source = "Invalid input"
        expected = "Expected output"
        test_compose_expanded(source, expected)
